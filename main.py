import yfinance as yf
import pandas as pd
import time
import csv

def get_tickers() -> pd.DataFrame:
    url = 'https://en.m.wikipedia.org/wiki/List_of_S%26P_500_companies'
    return pd.read_html(url, attrs={'id': 'constituents'}, index_col='Symbol')[0]

undervalued_stocks = []
ticker_data = get_tickers()
ticker_symbols = ticker_data.index.to_list()
#ticker_symbols = ["KEY","MO","T"]

forecast_years = 5
#average_fcf_growth = 0.05
discount_rate = 0.15
terminal_value_multiplier = 10

# Fetch the stock data
for ticker_symbol in ticker_symbols:

    time.sleep(0.5)
    print(ticker_symbol)

    try:
        stock = yf.Ticker(ticker_symbol)
        last_price = stock.history(period="1d")["Close"].iloc[-1]
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
    average_fcf_growth = ( last_cashflow / first_cashflow ) ** ( 1 / 3  )  - 1 #Growth rate over last 4 years
    forecasted_fcf = [ last_cashflow  * ( 1 + average_fcf_growth ) ** i for i in range(1,forecast_years + 1) ]
    terminal_value = forecasted_fcf[-1] * terminal_value_multiplier
    forecasted_fcf.append(terminal_value)
    discounted_fcf = [ fcf / ( 1 + discount_rate ) ** i for i, fcf in enumerate(forecasted_fcf,1) ]
    fair_value = sum(discounted_fcf)
    fair_value_share = fair_value / shares_outstanding
    
    if last_price < fair_value_share:
        delta = (fair_value_share - last_price) / last_price * 100
        print(ticker_symbol)
        print(last_price)
        print(fair_value_share)
        print(delta)
        data = { "Ticker":ticker_symbol, "Last price" : last_price, "Fair value" : fair_value_share, "Delta %" : delta }
        undervalued_stocks.append(data)
        

print("Analysis ended")
print("Writing to file")

columns = ["Ticker", "Last price", "Fair value", "Delta %"]

with open("output.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()  # Write column names
    writer.writerows(undervalued_stocks)  # Write rows


