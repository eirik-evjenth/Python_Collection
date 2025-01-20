import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import csv


filnavn = "Visual Studio IT 2/Kapittel 3/Kapittel 3B/CSV files/Lonn 2015-2020.csv"

# Lister for å ta vare på alle årstall og gjennomsnittslønn for menn og kvinner
aarstall = []
mann_lonn = []
kvinne_lonn = []

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    
    overskrifter = next(filinnhold)
    print(overskrifter)
    
    for rad in filinnhold:
        if rad[2] == "Menn":
            aarstall.append(int(rad[4]))
            mann_lonn.append(int(rad[5]))
        elif rad[2] == "Kvinner":
            kvinne_lonn.append(int(rad[5]))

# Tegner grafen
plt.plot(aarstall, mann_lonn, label="Menn")
plt.plot(aarstall, kvinne_lonn, label="Kvinner")
plt.xlabel("År")
plt.ylabel("Gjennomsnitt Maanedslnn (kr)")
plt.legend()
plt.grid()
plt.show()