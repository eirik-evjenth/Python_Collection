import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

filnavn = "Visual Studio IT 2\\Kapittel 3\\Kapittel 3B\\CSV files\\Lonn 2015-2020.csv"

# Lister for å ta vare på alle årstall og gjennomsnittslønn for menn og kvinner
aarstall = []
mann_lonn = []
kvinne_lonn = []

try:
    with open(filnavn, encoding="utf-8-sig") as fil:
        filinnhold = csv.reader(fil, delimiter=";")
        
        overskrifter = next(filinnhold)
        print("Headers:", overskrifter)
        
        for rad in filinnhold:
            print("Row:", rad)  # Debugging statement to check each row
            if rad[2] == "Menn":
                aarstall.append(int(rad[4]))
                mann_lonn.append(int(rad[5]))
            elif rad[2] == "Kvinner":
                kvinne_lonn.append(int(rad[5]))
except FileNotFoundError:
    print(f"File not found: {filnavn}")
except Exception as e:
    print(f"An error occurred: {e}")

# Convert lists to numpy arrays for easier manipulation
aarstall = np.array(aarstall)
mann_lonn = np.array(mann_lonn)
kvinne_lonn = np.array(kvinne_lonn)

# Create a grouped bar chart
bar_width = 0.35
index = np.arange(len(aarstall))

plt.bar(index, mann_lonn, bar_width, label="Menn")
plt.bar(index + bar_width, kvinne_lonn, bar_width, label="Kvinner")

plt.xlabel("År")
plt.ylabel("Gjennomsnitt Maanedslnn (kr)")
plt.title("Lønnsutvikling for Menn og Kvinner (2015-2020)")
plt.xticks(index + bar_width / 2, aarstall)
plt.legend()
plt.grid()
plt.show()
