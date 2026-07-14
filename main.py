from data import get_prices
from strategy import run_momentum
from metrics import performance_table
from plotting import plot_performance
 
tickers = [
    'AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL',
    'META', 'TSLA', 'JPM', 'V', 'NFLX',
    'JNJ', 'PFE', 'XOM', 'CAT', 'COST',
    'WMT', 'BA', 'GE', 'PG', 'AXP'
]
 
monthly_prices, monthly_returns = get_prices(tickers, period = '5y')
strategy_returns = run_momentum(monthly_prices, monthly_returns)
benchmark_returns = monthly_returns.mean(axis = 1)
 
table, cum_strategy, cum_benchmark = performance_table(strategy_returns, benchmark_returns)
print(table)
 
plot_performance(cum_strategy, cum_benchmark)