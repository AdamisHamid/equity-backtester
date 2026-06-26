import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'JPM', 'V', 'NFLX']
close = yf.download(tickers, period = '3y')['Close']

print(close.shape)
print(close.head())