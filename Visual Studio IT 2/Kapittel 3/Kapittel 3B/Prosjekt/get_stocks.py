import yfinance as yf


data = yf.download("AAPL", start="1980-12-12", end="2024-02-13")


data.to_csv("AAPL_max.csv")