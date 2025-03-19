
import csv
import matplotlib.pyplot as plt

# Open the CSV file
with open('run_ww_2020_w-PROVE.csv', 'r') as file:
    # Read the CSV file
    reader = csv.DictReader(file)
    
    # Opprettar 2 ordbøker/dictionaries for å lagre nødvendig informasjon
    duration_per_week = {}
    date_to_week = {}
    
    # Variablar for å handtere vekenummer
    current_week = None
    week_number = 0
    
    # Summer "duration" for kvar veke, og map kvar dato til eit vekenummer
    for row in reader:
        week = row['datetime']
        if week != current_week:
            current_week = week
            week_number += 1
        duration = float(row['duration'])
        duration_per_week[week] = duration_per_week.get(week, 0) + duration # Hugs fordelane med get
        date_to_week[week] = f"Week {week_number}"


max_week = max(duration_per_week, key=duration_per_week.get)
max_duration_minutes = duration_per_week[max_week]
max_week_label = date_to_week[max_week]

max_duration_days = max_duration_minutes / (60*24)
max_duration_years = max_duration_days / 365


print(f"Max duration: {max_duration_years:.2f} years in {max_week_label}")



# Finn veka med høgaste "duration" (kunne eventuelt gjort dette i for-løkka over)
max_week = max(duration_per_week, key=duration_per_week.get)

# Lag ein ny figur med ein spesifisert størrelse
plt.figure(figsize=(15, 9))

# Lag eit bar plot for "duration" per veke
weeks = list(date_to_week.values())
durations = list(duration_per_week.values())



color = ['red' if week == f"{max_week_label}" else 'blue' for week in weeks]

plt.bar(weeks, durations, color=color)
plt.xlabel('Veke')
plt.ylabel('Aktivitet')
plt.title(f'Veke med høgast aktivitet: {max_week}')
plt.xticks(rotation=90)  # Roter labels på x-aksen
plt.subplots_adjust(bottom=0.2)
plt.show()