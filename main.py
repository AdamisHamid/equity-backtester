import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'JPM', 'V', 'NFLX']
close = yf.download(tickers, period = '3y')['Close']

monthly_prices = close.resample('ME').last()
monthly_returns = monthly_prices.pct_change().dropna()

momentum = monthly_prices.pct_change(12)