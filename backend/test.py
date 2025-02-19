import yfinance as yf 
import pandas as pd

df = pd.read_csv("output.csv")
filtered_data = df[df["ticker"] == 'CE']
print(filtered_data)

