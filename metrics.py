import pandas as pd
 
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
 
def performance_table(strategy_returns, benchmark_returns, years = 5):
    cum_strategy  = (1 + strategy_returns.dropna()).cumprod()
    cum_benchmark = (1 + benchmark_returns.dropna()).cumprod()
 
    total_return_strategy = cum_strategy.iloc[-1] - 1
    total_return_benchmark = cum_benchmark.iloc[-1] - 1
 
    annualised_return_strategy = (cum_strategy.iloc[-1] ** (1 / years)) - 1
    annualised_return_benchmark = (cum_benchmark.iloc[-1] ** (1 / years)) - 1
 
    sharpe_strategy  = sharpe_ratio(strategy_returns.dropna())
    sharpe_benchmark = sharpe_ratio(benchmark_returns.dropna())
 
    max_drawdown_strategy  = max_drawdown(cum_strategy)
    max_drawdown_benchmark = max_drawdown(cum_benchmark)
 
    table = pd.DataFrame({
        'Metric': ['Total Return', 'Annualised Return', 'Sharpe Ratio', 'Max Drawdown'],
        'Strategy': [total_return_strategy, annualised_return_strategy, sharpe_strategy, max_drawdown_strategy],
        'Benchmark': [total_return_benchmark, annualised_return_benchmark, sharpe_benchmark, max_drawdown_benchmark]
    })
 
    return table, cum_strategy, cum_benchmark