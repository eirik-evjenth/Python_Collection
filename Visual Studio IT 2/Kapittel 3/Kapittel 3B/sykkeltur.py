'''
a)
Lag et program som presenterer de tre mest brukte startlokasjonene og de tre minst 
brukte startlokasjonene. Presentasjonen skal også vise antall turer fra disse startlokasjonene.

b)
Utvid programmet slik at det også presenterer et passende diagram som viser totalt antall turer 
fra alle startlokasjoner til sammen, per ukedag.
'''

# import pandas as pd
import matplotlib.pyplot as plt
import csv


filnavn = "CSV files\Sykkeltur.csv"
# df = pd.read_csv(filnavn, delimiter=";", encoding="utf-8")

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=",")

    start_stations = []

    for start_station in filinnhold:
        if start_station not in start_stations:
            start_stations.append(start_station)
            # print("hello")

# number_of_starts = []

# for start_station in start_stations:
#     number = start_station.count()
#     number_of_starts.append(number)


# sorted_numbers = number_of_starts.sort()

# top_three_starts = sorted_numbers[:3]
# bottom_three_starts = sorted_numbers[-3:]

