# 1

import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from datetime import datetime


file = "run_ww_2020_w-PROVE.csv" # finner filen

df = pd.read_csv(file)

age_group_counts = df['age_group'].value_counts()
print(f"Age group counts:\n{age_group_counts}\n")

# 2

def thousands(x, pos):
    return '%1.1fK' % (x * 1e-3)

age_groups = df['age_group'].unique()

counts = [age_group_counts.get(age_group, 0) for age_group in age_groups]

plt.title('Runners in age groups')
plt.ylabel('Antall')
plt.xlabel('Age group')
plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands)) 
plt.bar(age_groups, counts)
plt.show()

# 3

'''
For aktivitetsnivå bruker jeg distanse kilometer, siden en distanse krever cirka like mange kalorier å løpe som det gjør
med å bare gå. Så hvis noen går en hvis distanse vil hastigheten ikke ha så mye betydning for total aktivitet.
Ser på hvilket uke hadde størst total distanse.
'''
# Convert 'datetime' column to datetime type
df['datetime'] = pd.to_datetime(df['datetime'])

# Extract week number from 'datetime' column
df['week'] = df['datetime'].dt.isocalendar().week

# Group by week and sum the duration
weekly_duration = df.groupby('week')['duration'].sum()

# Find the week with the maximum duration
max_week = weekly_duration.idxmax()
max_duration_minutes = weekly_duration.max()

'''
# Convert duration to days and years
max_duration_days = max_duration_minutes / (60 * 24)
max_duration_years = max_duration_days / 365

print(f"Max duration: {max_duration_years:.2f} years in Week {max_week}")
'''


color = ['red' if week == max_week else 'blue' for week in weekly_duration.index]

plt.bar(weekly_duration.index, weekly_duration.values, color=color)
plt.xlabel('Week')
plt.ylabel('Activity (minutes)')
plt.title(f'Week with highest activity: Week {max_week}')
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.2)
plt.show()

# 4

'''
Egen oppgave hvor jeg vil finne ut hvilket Major har løpt lengst.
'''

Majors = df['major'].unique()

major_durations = df.groupby('major')['duration'].sum()

for major, duration in major_durations.items():
    #print(f"{major}: {duration} minutes")
    pass
