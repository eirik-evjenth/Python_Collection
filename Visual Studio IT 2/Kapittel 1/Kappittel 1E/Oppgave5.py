'''
    5. Lag en ordbok der nøklene er land og verdiene er antall innbyggere. 
    Legg inn informasjon om de fem landene med flest innbyggere i verden.

    a) Skriv ut en oversikt med navnene til alle landene ved hjelp av en løkke.
    b) Skriv ut en oversikt med bare innbyggertallene til alle landene.
    c) Skriv ut en tekst om hvert land på formen: «X har Y innbyggere».
    d) Bruk sorted() for å skrive ut lista i oppgave c med landenes navn i alfabetisk rekkefølge. 
       (Hint: sorted(land.keys()))
    e) Gå gjennom alle landene og avslutt med en tekst på formen: «X har flest innbyggere. 
       Y har færrest innbyggere.»
'''

# a)

ordbok = {
"India": 1450935000, 
"China": 1419321000, 
"United States": 345426000, 
"Indonesia": 283487000, 
"Pakistan": 251269000
}

for x in ordbok:
   print(x)
print()

# b)

for x in ordbok:
    print(ordbok[x])
print()

# c) 
   
for x in ordbok:
   print(f"{x} har {ordbok[x]} innbyggere")
print()

# d)

sortert = sorted(ordbok.keys())
for x in sortert:
   print(f"{x} har {ordbok[x]} innbyggere")
print()

# e)

størst = 0
minst = 999999999999

for land, innbyggere in ordbok.items(): # Har to ting i for løken sann at vi lagrer begge verdiene for senere bruk
    if innbyggere > størst:
        størst = innbyggere
        størst_land = land
    if innbyggere < minst:
        minst = innbyggere
        minst_land = land

print(f"{minst_land} har færrest innbyggere, og {størst_land} har flest innbyggere")


