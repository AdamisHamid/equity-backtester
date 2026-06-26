import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'JPM', 'V', 'NFLX']
close = yf.download(tickers, period = '3y')['Close']

monthly_prices = close.resample('ME').last()
monthly_returns = monthly_prices.pct_change().dropna()

momentum = monthly_prices.pct_change(12).shift(1)
ranks = momentum.rank(axis = 1, ascending = False)

signal = ranks.shift(1)
top3 = signal <= 3

strategy_returns = (top3 * monthly_returns).mean(axis = 1)

turnover = top3.astype(float).diff().abs().sum(axis = 1) / 2
transaction_costs = turnover * 0.001
strategy_returns = strategy_returns - transaction_costs

def sharpe_ratio(returns):
    return returns.mean() / returns.std() * (12 ** 0.5)


def max_drawdown(portfolio_values):
    portfolio_values = list(portfolio_values)
    peak = portfolio_values[0]
    worst_drawdown = 0
    
    for value in portfolio_values: 
        if value > peak:
            peak = value
        drawdown = round((value - peak) / peak, 2)
        if drawdown < worst_drawdown:
            worst_drawdown = drawdown

    return worst_drawdown

cum_strategy = (1 + strategy_returns.dropna()).cumprod()
cum_benchmark = (1 + monthly_returns.mean(axis = 1).dropna()).cumprod()


