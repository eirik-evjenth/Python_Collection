'''
1. Lag en funksjon som tar en streng som parameter og returnerer en ny streng der alle vokalene er fjernet.
2. Lag en funksjon som tar en streng som parameter og returnerer True hvis strengen er et palindrom, ellers False.
3. Lag en funksjon som tar en liste av tall som parameter og returnerer en ny liste der alle negative tall er fjernet.
'''

# 1. Lag en funksjon som tar en streng som parameter og returnerer en ny streng der alle vokalene er fjernet.

tekst1 = input("Skriv noe: ")       # Her skriver brukeren noe

def vokal_remover(tekst1):
    vokaler = "aeiouæAEIOUÆ"       #Alle vokaler
    ny_tekst1 = ""                  # Teksten som vi skal sette alt som er ikke vokaler i
    
    for bokstav in tekst1:          # Sjekker hver bokstav
        if bokstav not in vokaler: # Sjekker om bokstaven er i vokalene våre
            ny_tekst1 += bokstav    # Hvis det er ikke så tar vi det i den nye teksten
     
    return ny_tekst1

print(vokal_remover(tekst1))


# 2. Lag en funksjon som tar en streng som parameter og returnerer True hvis strengen er et palindrom, ellers False.

tekst2 = input("Skriv noe: ")

def  palindrom_sjekker(tekst2):
    palindrom = False
    tekst2_reverse = tekst2[::-1]
    if tekst2.lower() == tekst2_reverse.lower():
        palindrom = True

    return palindrom

print(palindrom_sjekker(tekst2))

        
# 3. Lag en funksjon som tar en liste av tall som parameter og returnerer en ny liste der alle negative tall er fjernet.

tall_liste_lengde = 0
tall_liste = []

while len(tall_liste) < 5:
    tall3 = int(input("Skriv inn et tall: "))
    tall_liste.append(tall3)

def positive_tall(tall_liste):
    for tall in tall_liste:
        if tall < 0:
            tall_liste.pop(tall_liste.index(tall))
    return tall_liste

print(positive_tall(tall_liste))