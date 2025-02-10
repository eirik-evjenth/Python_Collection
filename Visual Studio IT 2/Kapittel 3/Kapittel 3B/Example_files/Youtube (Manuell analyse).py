import json
import matplotlib.pyplot as plt

filnavn = "Json files\Youtube.json"

with open(filnavn, encoding="utf-8") as fil:
    data = json.load(fil)

for creation in data:
    creation = int(creation["created_year"])
    if creation > 2019:
        print(creation["Youtuber"])

'''
youtuber_count = 0


# For youtubere med en viss antall subscribers
for youtuber in data:
    if youtuber["subscribers"] > 50000000:
        # print(f"{youtuber['Youtuber']} has the rank {youtuber['rank']}") # for printing in terminal
        youtuber_count += 1

# For youtubere med en viss rank
for youtuber in data:
    if youtuber["rank"] < 51:
        youtuber_count += 1

top_youtubers = sorted(data, key=lambda x: x["subscribers"], reverse=True)[:youtuber_count]

names = [youtuber["Youtuber"] for youtuber in top_youtubers]
subscribers = [youtuber["subscribers"] for youtuber in top_youtubers]

plt.figure(figsize=(12, 8))
# plt.bar(names, subscribers, color='blue') # for vertical bars
plt.barh(names, subscribers, color='blue') # For horisontal bars
plt.xlabel('Subscribers')
plt.title(f'Top {youtuber_count} Youtubers by Subscribers')
# plt.gca().invert_yaxis() # Flipper aksene
plt.show()
'''