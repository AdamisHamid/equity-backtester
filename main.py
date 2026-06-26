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
        drawdown = (value - peak) / peak
        if drawdown < worst_drawdown:
            worst_drawdown = drawdown

    return worst_drawdown

cum_strategy = (1 + strategy_returns.dropna()).cumprod()
cum_benchmark = (1 + monthly_returns.mean(axis = 1).dropna()).cumprod()

total_return_strategy = cum_strategy.iloc[-1] - 1
total_return_benchmark = cum_benchmark.iloc[-1] - 1

annualised_return_strategy = (cum_strategy.iloc[-1] ** (1 / 3)) - 1
annualised_return_benchmark = (cum_benchmark.iloc[-1] ** (1 / 3)) - 1

sharpe_strategy = sharpe_ratio(strategy_returns.dropna())
sharpe_benchmark = sharpe_ratio(monthly_returns.mean(axis = 1).dropna())

max_drawdown_strategy = max_drawdown(cum_strategy)
max_drawdown_benchmark = max_drawdown(cum_benchmark)

table = pd.DataFrame({
    'Metric': ['Total Return', 'Annualised Return', 'Sharpe Ratio', 'Max Drawdown'],
    'Strategy': [total_return_strategy, annualised_return_strategy, sharpe_strategy, max_drawdown_strategy],
    'Benchmark': [total_return_benchmark, annualised_return_benchmark, sharpe_benchmark, max_drawdown_benchmark]
})

print(table)