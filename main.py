import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'JPM', 'V', 'NFLX']
close = yf.download(tickers, period = '3y')['Close']

monthly_prices = close.resample('ME').last()
monthly_returns = monthly_prices.pct_change().dropna()

momentum = monthly_prices.pct_change(12)
ranks = momentum.rank(axis = 1, ascending = False)

signal = ranks.shift(1)
top3 = signal <= 3

strategy_returns = (top3 * monthly_returns).mean(axis = 1)

turnover = top3.astype(float).diff().abs().sum(axis=1) / 2
transaction_costs = turnover * 0.001
strategy_returns = strategy_returns - transaction_costs

