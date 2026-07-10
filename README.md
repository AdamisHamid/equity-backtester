# Equity Backtesting Engine — v0

This is a momentum-based equity backtesting engine built in Python. It works by buying the top 3 performing stocks by a 12-month return each month and it rebalances monthly. 

## How it works 

Each month, the strategy ranks 10 US stocks by their 12-month returns. The top 3 performing stocks are then bought equally weighted and held for a month. At the end of the month, the strategy rebalances by selling the current holdings and buying the new top 3 performing stocks, and a 0.1% transactional cost is applied each time holdings change.

The signal is shifted by one month to avoid lookahead bias, so last month's momentum would decide this month's holdings.

## Universe

AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA, JPM, V, NFLX (Apple, Microsoft, Nvidia, Amazon, Google, Meta, Tesla, JP Morgan, Visa, Netflix)

## Results (June 2023 – June 2026)

| Metric             | Strategy | Benchmark |
|--------------------|----------|-----------|
| Total Return       | 15.7%    | 111.9%    |
| Annualised Return  | 5.0%     | 28.5%     |
| Sharpe Ratio       | 0.86     | 1.46      |
| Max Drawdown       | -5.4%    | -13.2%    |

## Performance Chart

![Performance](performance.png)

## Observations

The momentum strategy significantly underperformed the equal-weight 
benchmark over the 3-year period (15.7% vs 111.9% total return). 
However, the strategy had a considerably lower max drawdown (-5.4% 
vs -13.2%), suggesting it was more conservative in avoiding large losses.

The Sharpe ratio (0.86) indicates the strategy generated modest 
risk-adjusted returns but still fell short of the benchmark (1.46). 
This is likely due to the limited universe of 10 stocks and the simple 
12-month momentum signal without additional filters.

v1 will address this by adding walk-forward testing to validate the 
strategy out-of-sample and low volatility as a second signal alongside 
momentum.

## How to run

pip install yfinance pandas matplotlib

python main.py

## What's next (v1)

- Expand universe from 10 to 20 stocks
- Walk-forward testing to validate the strategy out-of-sample
- Add low volatility as a second signal alongside momentum