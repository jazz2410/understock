import yfinance as yf
import pandas as pd
import datetime
import time
import csv
import requests

def get_tickers() -> list:
    
    def get_sp500_tickers() -> list:
        url = 'https://en.m.wikipedia.org/wiki/List_of_S%26P_500_companies'
        sp500 = pd.read_html(url, attrs={'id': 'constituents'})[0]
        return sp500.iloc[:, 0].tolist()  # Convert first column to a list

    def get_eurostoxx50_tickers() -> list:
        url = 'https://en.m.wikipedia.org/wiki/EURO_STOXX_50'
        tables = pd.read_html(url)
        
        for table in tables:
            if "Ticker" in table.columns:
                return table["Ticker"].tolist()  # Convert "Ticker" column to a list

        # Fetch tickers
    sp500_tickers = get_sp500_tickers()
    eurostoxx50_tickers = get_eurostoxx50_tickers()

    # Combine both lists into one structure
    all_tickers = sp500_tickers + eurostoxx50_tickers  
    return all_tickers

def run(ticker_data):
    
    undervalued_stocks = []
    ticker_symbols = ticker_data
    
    forecast_years = 5
    discount_rate = 0.15
    terminal_value_multiplier = 10
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    bond_yield = get_aaa_bond_yield()  # Fetch AAA bond yield

    # Fetch the stock data
    for ticker_symbol in ticker_symbols:


        time.sleep(0.5)
        print(ticker_symbol)

        try:
            stock = yf.Ticker(ticker_symbol)
            last_price = stock.history(period="1d")["Close"].iloc[-1]
            last_price = round(last_price,2)
            stock_name = stock.info.get("longName", "Name not found")
            cash_flow = stock.cashflow
            eps = stock.info.get("trailingEps", 0)
        except Exception as e:
            print("No data found")
            continue

        try:
            free_cashflow = cash_flow.loc["Free Cash Flow"]
            shares_outstanding = stock.info['sharesOutstanding']  # Total shares outstanding
            forward_pe_ratio = stock.info.get("forwardPE")
        except KeyError:
            print("Error for missing data in operating cash flow,CapEx or outstanding shares.")
            continue
        
        if forward_pe_ratio > 15:
            continue

        cashflow = free_cashflow
        last_cashflow = cashflow.iloc[0]
        first_cashflow = cashflow.iloc[3]
        historic_fcf_growth = ( last_cashflow / first_cashflow ) ** ( 1 / 3  )  - 1 #Growth rate over last 4 years
    
        if last_cashflow < 0:
            continue
    
        if isinstance(historic_fcf_growth,complex):
            continue
    
        if historic_fcf_growth > 0.05:
            future_fcf_growth = 0.05
        else:
            future_fcf_growth = historic_fcf_growth
        
        forecasted_fcf = [ last_cashflow  * ( 1 + future_fcf_growth ) ** i for i in range(1,forecast_years + 1) ]
        terminal_value = forecasted_fcf[-1] * terminal_value_multiplier
        forecasted_fcf.append(terminal_value)
        discounted_fcf = [ fcf / ( 1 + discount_rate ) ** i for i, fcf in enumerate(forecasted_fcf,1) ]
        fair_value = sum(discounted_fcf)
        fair_value_share = fair_value / shares_outstanding
        if isinstance(fair_value_share,complex):
            continue
        fair_value_share = round(fair_value_share,2)
        
        ###Begin of Graham evaluation#####################################
        if eps < 0:
            continue
        fair_value_graham = (eps * (8.5 + 2 * future_fcf_growth) * 4.4) / bond_yield
        fair_value_graham = round(fair_value_graham,2)
        delta_graham = (fair_value_graham - last_price) / last_price * 100
        delta_graham = round(delta_graham,1)
        ##End of Graham evaluation#########################################
        
        if last_price < fair_value_share or last_price < fair_value_graham:
            delta = (fair_value_share - last_price) / last_price * 100
            delta = round(delta,1)
            print(ticker_symbol)
            print(last_price)
            print(fair_value_share)
            print(historic_fcf_growth)
            print(future_fcf_growth)
            print(delta)
            data = { "ticker":ticker_symbol,"stockName" : stock_name, "lastPrice" : last_price,"eps" : eps, "fairValue" : fair_value,"fairValueShare" : fair_value_share,"fairValueGraham" : fair_value_graham,"sharesOutstanding" : shares_outstanding, "historic_fcf_growth" : historic_fcf_growth,"future_fcf_growth" : future_fcf_growth, "delta" : delta,"delta_graham" : delta_graham,"last_cf" : last_cashflow,"fcf_1" : forecasted_fcf[0], "fcf_2" : forecasted_fcf[1], "fcf_3" : forecasted_fcf[2], 'fcf_4' : forecasted_fcf[3], 'fcf_5' : forecasted_fcf[4],'fcf_6' : forecasted_fcf[5],"dcf_1" : discounted_fcf[0], "dcf_2" : discounted_fcf[1], "dcf_3" : discounted_fcf[2], "dcf_4" : discounted_fcf[3], "dcf_5" : discounted_fcf[4],"dcf_6" : discounted_fcf[5],"bondYield" : bond_yield, "timestamp" : timestamp }
            undervalued_stocks.append(data)
            

    print("Analysis ended")
    print("Writing to file")

    columns = ["ticker","stockName", "lastPrice","eps", "fairValue","fairValueShare","fairValueGraham","sharesOutstanding","historic_fcf_growth","future_fcf_growth", "delta","delta_graham","last_cf","fcf_1","fcf_2","fcf_3","fcf_4","fcf_5","fcf_6","dcf_1","dcf_2","dcf_3","dcf_4","dcf_5","dcf_6","bondYield","timestamp"]

    path = "/var/www/understock/script/output.csv"
    #path = "output.csv"

    with open(path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()  # Write column names
        writer.writerows(undervalued_stocks)  # Write rows
        

def get_aaa_bond_yield():

    try:
        response = requests.get("https://fred.stlouisfed.org/data/AAA.txt")  # Example source
        if response.status_code == 200:
            return float(response.text.strip().split()[-1])  # Extract latest value
    except:
        pass
    return 4.4  # Default value if API fails

        
if __name__ == "__main__":
    ticker_data = get_tickers()
    run(ticker_data)


