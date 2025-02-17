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

# Get balance sheet data
operating_cashflow = stock.cash_flow.loc["Cash Flow From Continuing Operating Activities"]
capital_expenditure = stock.cash_flow.loc["Capital Expenditure"]
shares_outstanding = stock.info['sharesOutstanding']  # Total shares outstanding

cashflow = operating_cashflow + capital_expenditure
last_cashflow = cashflow.iloc[0]
fcf_cashflow = [ last_cashflow  * ( 1 + average_fcf_growth ) ** i for i in range(1,forecast_years + 1) ]
terminal_value = fcf_cashflow[-1] * terminal_value_multiplier
fcf_cashflow.append(terminal_value)
discounted_fcf = [ fcf / ( 1 + discount_rate ) ** i for i, fcf in enumerate(fcf_cashflow,1) ]

fair_value = sum(discounted_fcf)
fair_value_share = fair_value / shares_outstanding
print(fair_value)
print(shares_outstanding)
print(fair_value_share)
fair_value_share = round(fair_value_share,2)
print(fair_value_share)
print(type(fair_value))
print(type(fair_value_share))