'''
# 2

Lag en ordbok som lar deg gjøre om fra tallene 1, 2, 3, … , 10 til tekstene «en», «to», «tre», …, «ti».

Skriv ut alle tallene med sine tilhørende tekster i tabellform.
Test ordboka ved å la en bruker skrive inn et tall.

tall = {  
    "1":  "en",
    "2":  "to",
    "3":  "tre",
    "4":  "fire", 
    "5":  "fem",
    "6":  "seks",
    "7":  "syv",
    "8":  "åtte",
    "9":  "ni",
    "10": "ti"
}

for x in tall:
    print(f"{x} : {tall[x]}")

bruker_test = input("Skriv inn et tall fra 1 - 10: ")

for x in tall:
    if bruker_test == x:
        print(f"Tilsvarende verdi med bokstaver: {tall[x]}")


# 3

tekst = input("Skriv noe: ")
tekst = tekst.lower()

bokstav_frekvens = {}


for bokstav in tekst:
    if bokstav in bokstav_frekvens:
        bokstav_frekvens[bokstav] += 1
    else:
        bokstav_frekvens[bokstav] = 1

sorterte_bokstaver = sorted(bokstav_frekvens.items())

print("Bokstav | Antall forekomster")
print("-----------------------------")

for bokstav, antall in sorterte_bokstaver:
    print(f"{bokstav:8} | {antall:20}")
print()
'''

# 4

'''
norskeByer = {
    "Oslo": "Hovedstaden i Norge og landets største by. Oslo er kjent for sine kulturelle tilbud, vakre parker og moderne arkitektur, og er et sentrum for norsk politikk og økonomi.",

    "Bergen": "Norges nest største by, ofte kalt 'byen mellom de syv fjell.' Bergen er kjent for sin historiske brygge, regnværsdager og som inngangsporten til de majestetiske fjordene på Vestlandet.",

    "Trondheim": "En sjarmerende universitetsby som tidligere var Norges hovedstad. Trondheim er kjent for sin historiske Nidarosdomen, som er et viktig pilegrimsmål, og for sin livlige studentkultur."

}

for byer in norskeByer:
    print(f"{byer}:")
    print(norskeByer[byer])
    print()
    '''

# 5
eliteserielag = [

  { "lag": "Lillestrøm", "seriemesterskap": [1976, 1977, 1986, 1989], "norgesmesterskap": [1977, 1978, 1981, 1985, 2007, 2017] },
  { "lag": "Molde", "seriemesterskap": [2011, 2012, 2014, 2019], "norgesmesterskap": [1994, 2005, 2013, 2014, 2021] },
  { "lag": "Viking", "seriemesterskap": [1972, 1973, 1974, 1975, 1979, 1982, 1991], "norgesmesterskap": [1979, 1989, 2001, 2019] },
  { "lag": "Strømsgodset", "seriemesterskap": [1970, 2013], "norgesmesterskap": [1969, 1970, 1973, 1991, 2010] },
  { "lag": "Aalesund", "seriemesterskap": [], "norgesmesterskap": [2009, 2011] },
  { "lag": "Rosenborg", "seriemesterskap": [1967, 1969, 1971, 1985, 1988, 1990, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2009, 2010, 2015, 2016, 2017, 2018], "norgesmesterskap": [1964, 1971, 1988, 1990, 1992, 1995, 1999, 2003, 2015, 2016, 2018] },
  { "lag": "Sarpsborg", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Bodø/Glimt", "seriemesterskap": [2020, 2021], "norgesmesterskap": [1975, 1993] },
  { "lag": "Odd", "seriemesterskap": [], "norgesmesterskap": [2000] },
  { "lag": "Tromsø", "seriemesterskap": [], "norgesmesterskap": [1986, 1996] },
  { "lag": "Vålerenga", "seriemesterskap": [1965, 1981, 1983, 1984, 2005], "norgesmesterskap": [1980, 1997, 2002, 2008] },
  { "lag": "HamKam", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Sandefjord", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Haugesund", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Jerv", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Kristiansund", "seriemesterskap": [], "norgesmesterskap": [] }

]
'''
print("Land som har vunnet seriemesterskap: ")
for lag in eliteserielag:
    if len(lag["seriemesterskap"]) > 0:
        print(lag["lag"])
print()

print("Land som har vunnet norgesmesterskap: ")
for lag in eliteserielag:
    if len(lag["norgesmesterskap"]) > 0:
        print(lag["lag"])
print()

print("Land som har vunnet norgesmesterskap og seriemesterskap: ")
for lag in eliteserielag:
    if len(lag["norgesmesterskap"]) and len(lag["seriemesterskap"]) > 0:
        print(lag["lag"])
print()

størst = 0
minst = 9999
alle_minste = []
alle_størst = []

for lag in eliteserielag:
    if len(lag["norgesmesterskap"]) > størst:
        størst = len(lag["norgesmesterskap"])
        alle_størst.append(lag["lag"])
    elif len(lag["norgesmesterskap"]) < minst:
        minst = len(lag["norgesmesterskap"])
        if minst == 0:
            alle_minste.append(lag["lag"])
print(f"Land som har vunnet mest og minst norgesmesterskap: {alle_størst} har vunnet mest med {størst},\n",
       f"{alle_minste} har vunnet minst med {minst}")
print()


størst = 0
minst = float('inf')
alle_minste = []
alle_størst = []

for lag in eliteserielag:
    if len(lag["seriemesterskap"]) > størst:
        størst = len(lag["seriemesterskap"])
        alle_størst.append(lag["lag"])
    elif len(lag["seriemesterskap"]) < minst:
        minst = len(lag["seriemesterskap"])
        if minst == 0:
            alle_minste.append(lag["lag"])
print(f"Land som har vunnet mest og minst seriemesterskap: {alle_størst} har vunnet mest med {størst},\n",
       f"{alle_minste} har vunnet minst med {minst}")
print()


størst = 0
minst = float('inf')
alle_minste = []
alle_størst = []

for lag in eliteserielag:
    norgesmesterskap_count = len(lag["norgesmesterskap"])
    
    if norgesmesterskap_count > størst:
        størst = norgesmesterskap_count
        alle_størst = [lag["lag"]]  # Reset and add the current lag
    elif norgesmesterskap_count == størst:
        alle_størst.append(lag["lag"])  # Add to the existing list

    if norgesmesterskap_count < minst:
        minst = norgesmesterskap_count
        alle_minste = [lag["lag"]]  # Reset and add the current lag
    elif norgesmesterskap_count == minst:
        alle_minste.append(lag["lag"])  # Add to the existing list

print(f"Land som har vunnet mest og minst norgesmesterskap: {alle_størst} har vunnet mest med {størst},\n",
      f"{alle_minste} har vunnet minst med {minst}")
print()


# For seriemesterskap
størst = 0
minst = float('inf')
alle_minste = []
alle_størst = []

for lag in eliteserielag:
    seriemesterskap_count = len(lag["seriemesterskap"])
    
    if seriemesterskap_count > størst:
        størst = seriemesterskap_count
        alle_størst = [lag["lag"]]
    elif seriemesterskap_count == størst:
        alle_størst.append(lag["lag"])

    if seriemesterskap_count < minst:
        minst = seriemesterskap_count
        alle_minste = [lag["lag"]]
    elif seriemesterskap_count == minst:
        alle_minste.append(lag["lag"])

print(f"Land som har vunnet mest og minst seriemesterskap: {alle_størst} har vunnet mest med {størst},\n",
      f"{alle_minste} har vunnet minst med {minst}")
'''

første_mester = None
siste_mester = None
første_år = float('inf')
siste_år = 0

for lag in eliteserielag:
    seriemesterskap = lag["seriemesterskap"]
    
    if seriemesterskap:  # Sjekk om laget har vunnet seriemesterskap
        if min(seriemesterskap) < første_år:  # Finn første mester
            første_år = min(seriemesterskap)
            første_mester = lag["lag"]
        
        if max(seriemesterskap) > siste_år:  # Finn siste mester
            siste_år = max(seriemesterskap)
            siste_mester = lag["lag"]

print(f"Laget som vant serien første gang: {første_mester} i {første_år}")
print(f"Laget som vant serien sist: {siste_mester} i {siste_år}")

print()

første_NM = None
siste_NM = None
første_år = float('inf')
siste_år = 0

for lag in eliteserielag:
    norgesmesterskap = lag["norgesmesterskap"]
    
    if norgesmesterskap:  # Sjekk om laget har vunnet norgesmesterskap
        if min(norgesmesterskap) < første_år:  # Finn første mester
            første_år = min(norgesmesterskap)
            første_NM = lag["lag"]
        
        if max(norgesmesterskap) > siste_år:  # Finn siste mester
            siste_år = max(norgesmesterskap)
            siste_NM = lag["lag"]

print(f"Laget som vant serien første gang: {første_NM} i {første_år}")
print(f"Laget som vant serien sist: {siste_NM} i {siste_år}")