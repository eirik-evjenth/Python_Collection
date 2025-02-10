'''
a)
Lag et program som presenterer de tre mest brukte startlokasjonene og de tre minst 
brukte startlokasjonene. Presentasjonen skal også vise antall turer fra disse startlokasjonene.

b)
Utvid programmet slik at det også presenterer et passende diagram som viser totalt antall turer 
fra alle startlokasjoner til sammen, per ukedag.
'''

from datetime import datetime
import matplotlib.pyplot as plt
import csv


filnavn = "CSV files\Sykkeltur.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    reader = csv.reader(fil)
    next(reader) # Går forbi første linje
    data = list(reader)

start_stations = []

for row in data:
    start_station = row[4]
    start_stations.append(start_station)

# print(start_stations)


station_counts = {}

for station in start_stations:
    if station in station_counts:
        station_counts[station] += 1
    else:
        station_counts[station] = 1

# Sorterer ordboken etter antall turer
sorted_stations = sorted(station_counts.items(), key=lambda item: item[1]) # item[1] er antall turer i ordboken

top_three_starts = sorted_stations[-3:]
bottom_three_starts = sorted_stations[:3]
'''
print(f"De tre minst brukte startlokasjonene er:")
for station, count in bottom_three_starts:
    print(f"{station}: {count} turer")

print()

print(f"De tre mest brukte startlokasjonene er:")
for station, count in top_three_starts:
    print(f"{station}: {count} turer")
'''


start_dates = []
for row in data:
    split_row = row[0].split(' ') # Fjernar siste del
    date = split_row[0] # Datoen er den første delen av split_row (selve datoen ligger i rad 0, timer, minutt, sek etc. ligger i 1)
    start_dates.append(date) # Legg deretter til i start_dates

# Tell antall turer for hver ukedag
weekday_counts = [0, 0, 0, 0, 0, 0, 0]  # Mandag, tirsdag, onsdag, ...
for date in start_dates:
    weekday = datetime.strptime(date, "%Y-%m-%d").weekday() # Gjør tiden om til et objekt med strptime, så formatterer på YYYY-MM-DD, finner ukedagen etter det.
    weekday_counts[weekday] += 1

# Plot antall turer per ukedag
plt.bar(range(7), weekday_counts)
plt.xticks(range(7), ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag'])
plt.ylabel('Antall turer')
plt.title('Totale ant. turer fra alle startlokasjoner per ukedag')
plt.show()