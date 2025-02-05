import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

filnavn = "CSV files\\ecommerce_sales(CSV).csv"

product = []
quantity = []
price = []

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    
    overskrifter = next(filinnhold)
    print("Headers:", overskrifter)
    
    for rad in filinnhold:
        print("Row:", rad)
        if rad[5] == "Product":
            product.append(rad[5])
            quantity.append(int(rad[6]))
            price.append(int(rad[7]))

product = np.array(product)
quantity = np.array(quantity)
price = np.array(price)

# Create a grouped bar chart
bar_width = 0.35
index = np.arange(len(product))

plt.bar(index, product, bar_width, label="product")
plt.bar(index + bar_width, quantity, bar_width, label="quantity")

plt.xlabel("Product")
plt.ylabel("quantity")
plt.title("Salg av diverse produkter")
plt.xticks(index + bar_width / 2, product)
plt.legend()
plt.grid()
plt.show()
