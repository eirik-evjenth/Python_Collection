from datetime import datetime
import matplotlib.pyplot as plt
import csv

# https://www.kaggle.com/datasets/paultimothymooney/stock-market-data

file = "AAPL_max.csv"

with open(file, encoding="utf-8-sig") as fil:
    reader = csv.reader(fil)
    next(reader) # Går forbi første linje
    data = list(reader)

    # Extract dates and closing prices from the data
    dates = []
    closing_prices = []

    for row in data:
        dates.append(datetime.strptime(row[0], '%Y-%m-%d'))
        closing_prices.append(float(row[4]))

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(dates, closing_prices, label='Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.title('Apple Stock Closing Prices')
    plt.legend()
    plt.grid(True)
    plt.show()