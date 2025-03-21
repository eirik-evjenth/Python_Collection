import json

filnavn = "Visual Studio IT 2/Kapittel 3/Kapittel 3B/Json files/skandinavia.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

for land in data["land"]:
  print(f"\n{land['navn']}:")
  for navn in range(len(land["byer"])):
    print(f'{land["byer"][navn]}')