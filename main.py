from data import get_prices
from strategy import run_momentum, walk_forward_test
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
wf_returns = walk_forward_test(monthly_prices, monthly_returns)

table, cum_strategy, cum_benchmark, cum_wf = performance_table(strategy_returns, benchmark_returns, wf_returns)
print(table)

plot_performance(cum_benchmark, cum_strategy = cum_strategy, cum_wf = cum_wf, title = 'Momentum vs Walk-Forward vs Benchmark', filename = 'performance_v1.png')