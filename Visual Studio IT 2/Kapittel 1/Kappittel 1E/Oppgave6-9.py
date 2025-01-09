sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]

for x in sommer_ol:
    vinnerTid200m = x["vinnertider"]["200 m"]
    vinnerTid400m = x["vinnertider"]["400 m"]
    print(vinnerTid200m)
    print(vinnerTid400m)
print()
for x in sommer_ol:
    if x["årstall"] == 2020:
        print(x["vinnertider"])
print()

# Finn raskeste og sakteste tid på 200 m
raskest200m = 100000
sakteste200m = 0

for x in sommer_ol:
    if x["vinnertider"]["200 m"] < raskest200m:
        raskest200m = x["vinnertider"]["200 m"]
    elif x["vinnertider"]["200 m"] > sakteste200m:
        sakteste200m = x["vinnertider"]["200 m"]

print(f"Sakteste tid på 200 m: {sakteste200m}")
print(f"Raskeste tid på 200 m: {raskest200m}")

