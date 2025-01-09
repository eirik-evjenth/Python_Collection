sommer_ol = [
  { "øvelse": "100m", "årstall": { "2004": 10.93, "2008": 10.78, "2012": 10.75, "2016": 10.71, "2020": 10.61 } },
  { "øvelse": "200m", "årstall": { "2004": 22.06, "2008": 21.74, "2012": 21.88, "2016": 21.78, "2020": 21.53 } },
  { "øvelse": "400m", "årstall": { "2004": 49.41, "2008": 49.62, "2012": 49.55, "2016": 49.44, "2020": 48.36 } },
]

for x in sommer_ol:
    if x["øvelse"] == "400m":
        print(list(x["årstall"].values()))

for x in sommer_ol:
        print(x["årstall"]["2020"])

raskeste200m = float('inf')  # Start med en veldig stor verdi
sakteste200m = float('-inf')  # Start med en veldig lav verdi

for x in sommer_ol:
    if x["øvelse"] == "200m":
        for år, tid in x["årstall"].items():
            if tid < raskeste200m:
                raskeste200m = tid
            if tid > sakteste200m:
                sakteste200m = tid

'''
d)
    Likte når hver OL var delt opp istedenfor å dele med øvelsen.
'''