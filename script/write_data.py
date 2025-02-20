import yfinance as yf
import pandas as pd
import datetime
import time
import csv

def get_tickers() -> pd.DataFrame:
    url = 'https://en.m.wikipedia.org/wiki/List_of_S%26P_500_companies'
    return pd.read_html(url, attrs={'id': 'constituents'}, index_col='Symbol')[0]

undervalued_stocks = []
ticker_data = get_tickers()
ticker_symbols = ticker_data.index.to_list()

forecast_years = 5
discount_rate = 0.15
terminal_value_multiplier = 10
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

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
    except Exception as e:
        print("No data found")
        continue

    try:
        operating_cashflow = cash_flow.loc["Cash Flow From Continuing Operating Activities"]
        capital_expenditure = cash_flow.loc["Capital Expenditure"]
        shares_outstanding = stock.info['sharesOutstanding']  # Total shares outstanding
        forward_pe_ratio = stock.info.get("forwardPE")
    except KeyError:
        print("Error for missing data in operating cash flow,CapEx or outstanding shares.")
        continue
    
    if forward_pe_ratio > 15:
        continue

    cashflow = operating_cashflow + capital_expenditure
    last_cashflow = cashflow.iloc[0]
    first_cashflow = cashflow.iloc[3]
    historic_fcf_growth = ( last_cashflow / first_cashflow ) ** ( 1 / 3  )  - 1 #Growth rate over last 4 years
   
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
    
    if last_price < fair_value_share:
        delta = (fair_value_share - last_price) / last_price * 100
        delta = round(delta,1)
        print(ticker_symbol)
        print(last_price)
        print(fair_value_share)
        print(historic_fcf_growth)
        print(future_fcf_growth)
        print(delta)
        data = { "ticker":ticker_symbol,"stockName" : stock_name, "lastPrice" : last_price, "fairValue" : fair_value,"fairValueShare" : fair_value_share,"sharesOutstanding" : shares_outstanding, "historic_fcf_growth" : historic_fcf_growth,"future_fcf_growth" : future_fcf_growth, "delta" : delta,"last_cf" : last_cashflow,"fcf_1" : forecasted_fcf[0], "fcf_2" : forecasted_fcf[1], "fcf_3" : forecasted_fcf[2], 'fcf_4' : forecasted_fcf[3], 'fcf_5' : forecasted_fcf[4],'fcf_6' : forecasted_fcf[5],"dcf_1" : discounted_fcf[0], "dcf_2" : discounted_fcf[1], "dcf_3" : discounted_fcf[2], "dcf_4" : discounted_fcf[3], "dcf_5" : discounted_fcf[4],"dcf_6" : discounted_fcf[5], "timestamp" : timestamp }
        undervalued_stocks.append(data)
        

print("Analysis ended")
print("Writing to file")

columns = ["ticker","stockName", "lastPrice", "fairValue","fairValueShare","sharesOutstanding","historic_fcf_growth","future_fcf_growth", "delta","last_cf","fcf_1","fcf_2","fcf_3","fcf_4","fcf_5","fcf_6","dcf_1","dcf_2","dcf_3","dcf_4","dcf_5","dcf_6","timestamp"]

with open("output.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()  # Write column names
    writer.writerows(undervalued_stocks)  # Write rows


