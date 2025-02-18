import yfinance as yf 
import pandas as pd


forecast_years = 5
average_fcf_growth = 0.05
discount_rate = 0.15
terminal_value_multiplier = 10
# Define the stock ticker symbol
ticker_symbol = "AAPL"  # Replace with the desired stock symbol

# Fetch the stock data
stock = yf.Ticker(ticker_symbol)

stock_name = stock.info.get("longName", "Name not found")
print(stock_name)

# Get balance sheet data
operating_cashflow = stock.cash_flow.loc["Cash Flow From Continuing Operating Activities"]
capital_expenditure = stock.cash_flow.loc["Capital Expenditure"]
shares_outstanding = stock.info['sharesOutstanding']  # Total shares outstanding

