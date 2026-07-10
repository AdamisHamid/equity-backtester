import yfinance as yf
 
def get_prices(tickers, period = '3y'):
    close = yf.download(tickers, period = period)['Close']

    monthly_prices = close.resample('ME').last()
    monthly_returns = monthly_prices.pct_change().dropna()
    
    return monthly_prices, monthly_returns