import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol='AAPL', period='6mo', interval='1d'):
    data = yf.download(symbol, period=period, interval=interval)
    data.dropna(inplace=True)
    return data
