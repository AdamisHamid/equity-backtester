import pandas as pd

def run_momentum(monthly_prices, monthly_returns, top_n = 3, cost = 0.001):
    momentum = monthly_prices.pct_change(12).shift(1)
    ranks = momentum.rank(axis = 1, ascending = False)
    top_n_stocks = ranks <= top_n
 
    strategy_returns = (top_n_stocks * monthly_returns).mean(axis = 1)
 
    turnover = top_n_stocks.astype(float).diff().abs().sum(axis = 1) / 2
    transaction_costs = turnover * cost
    strategy_returns -= transaction_costs
 
    return strategy_returns

def walk_forward_test(monthly_prices, monthly_returns, train_window = 24, test_window = 6, top_n = 3, cost = 0.001):
    start = 0
    all_returns = []

    while start + train_window + test_window <= len(monthly_prices):
        training_slice = monthly_prices.iloc[start : start + train_window]
        test_slice = monthly_returns.iloc[start + train_window : start + train_window + test_window]

        momentum = training_slice.pct_change(12).shift(1)
        ranks = momentum.rank(axis = 1, ascending = False)
        latest_rank = ranks.iloc[-1]
        top_n_stocks = latest_rank <= top_n

        strategy_returns = (top_n_stocks * test_slice).mean(axis = 1)

        turnover = top_n_stocks.astype(float).sum() / 2 
        transaction_costs = turnover * cost
        strategy_returns.iloc[0] -= transaction_costs

        all_returns.append(strategy_returns)
        start += test_window

    combined = pd.concat(all_returns)

    return combined

def run_low_vol(monthly_returns, top_n = 3, cost = 0.001):
    volatility = monthly_returns.rolling(3).std().shift(1)
    ranks = volatility.rank(axis = 1, ascending = True)
    top_n_stocks = ranks <= top_n

    strategy_returns = (top_n_stocks * monthly_returns).mean(axis = 1)

    turnover = top_n_stocks.astype(float).diff().abs().sum(axis = 1) / 2
    transaction_costs = turnover * cost
    strategy_returns -= transaction_costs

    return strategy_returns