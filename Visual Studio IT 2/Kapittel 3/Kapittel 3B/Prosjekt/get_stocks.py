import yfinance as yf


NVDA_data = yf.download("NVDA", start="1999-01-22", end="2025-02-13")
data = yf.download("AAPL", start="1980-12-12", end="2025-02-13")
spy_data = yf.download('SPY', start='1980-12-12', end='2025-02-13')

spy_data.to_csv("S&P 500.csv")
data.to_csv("AAPL_max.csv")
NVDA_data.to_json("NVDA_max.json")


'''
Brukte dette først for å få aksjedataen til S&P 500 og Apple. 
Brukte Kaggle for å få en JSON fil med NVIDIA. Den hadde ikke alt dataen,
fordi av det prøvde jeg å bruke yahoo finance for det også, men lage det til en JSON fil.
Problemet er at det gir bare failed download requests og erstatter alt dataen jeg har med ingenting.
Derfor har jeg bare analysert det fra hånd.
'''