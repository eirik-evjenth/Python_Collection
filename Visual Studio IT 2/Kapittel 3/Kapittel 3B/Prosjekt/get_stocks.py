import yfinance as yf


NVDA_data = yf.download("NVDA", start="1999-01-22", end="2025-02-13")
data = yf.download("AAPL", start="1980-12-12", end="2025-02-13")
spy_data = yf.download('SPY', start='1980-12-12', end='2025-02-13')

spy_data.to_csv("S&P 500.csv")
data.to_csv("AAPL_max.csv")
NVDA_data.to_json("NVDA_max.json")