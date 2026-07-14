def run_momentum(monthly_prices, monthly_returns, top_n = 3, cost = 0.001):
    momentum = monthly_prices.pct_change(12).shift(1)
    ranks = momentum.rank(axis = 1, ascending = False)
    top_n_stocks = ranks <= top_n
 
    strategy_returns = (top_n_stocks * monthly_returns).mean(axis = 1)
 
    turnover = top_n_stocks.astype(float).diff().abs().sum(axis = 1) / 2
    transaction_costs = turnover * cost
    strategy_returns = strategy_returns - transaction_costs
 
    return strategy_returns