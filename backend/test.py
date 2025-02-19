import yfinance as yf 
import pandas as pd


ticker_symbol = 'GOOG'

try:
    stock = yf.Ticker(ticker_symbol)
    last_price = stock.history(period="1d")["Close"].iloc[-1]
    last_price = round(last_price,2)
    stock_name = stock.info.get("longName", "Name not found")
    cash_flow = stock.cashflow
except Exception as e:
    print("No data found")
    

