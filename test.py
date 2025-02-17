import yfinance as yf 
import pandas as pd

# Define the stock ticker symbol
ticker_symbol = "AAPL"  # Replace with the desired stock symbol

# Fetch the stock data
stock = yf.Ticker(ticker_symbol)

# Get balance sheet data
operating_cashflow = stock.cash_flow.loc["Cash Flow From Continuing Operating Activities"]
capital_expenditure = stock.cash_flow.loc["Capital Expenditure"]


#cash_flow = operating_cashflow + capital_expenditure
#print(cash_flow)
cash_flow = [100,200,300,400]
initial = cash_flow[3]
final = cash_flow[0]
print(initial)
print(final)
cagr = ( final / initial ) ** ( 1 / 3  )  - 1
print(cagr)
