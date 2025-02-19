from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Allow CORS for frontend (SvelteKit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # SvelteKit dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    df = pd.read_csv("output.csv")
    return df.to_dict(orient="records")

@app.get("/stock/{ticker}")
async def get_stock(ticker: str):
    df = pd.read_csv("output.csv")
    filtered_df = df[df['ticker'] == ticker]
    return filtered_df.to_dict(orient="records")
    