# 4 
'''
try:
    sidelengde = input("Skriv inn sidelengde av kvadratet: ")
    print()
    try:
         sidelengde = int(sidelengde)
         for i in range(sidelengde):
             
             print("#" * sidelengde)

    except ValueError:
        print("Ugyldig valg")
except KeyboardInterrupt:
    print("-")
    print("Du har avsluttet koden")

print()
'''

# 5

tekst = "Finn en litt lang norsk tekst, for eksempel fra Wikipedia eller en nettavis, og finn antall forekomster av bokstavene a, e og k. Er bokstavene like vanlige? Tilpass programmet slik at du kan sjekke antall forekomster av alle bokstaver i det norske alfabetet. (Hint: Lag en tekst med det norske alfabetet som du går gjennom med en løkke. Sjekk deretter teksten din mot hver av bokstavene.) Hvilke bokstaver er vanligst?"
bokstavA = "a"
bokstavE = "e"
bokstavK = "k"
A = 0
E = 0
K = 0

tekst = tekst.lower()

for bokstav in tekst:
    if bokstav == bokstavA:
        A += 1
    elif bokstav == bokstavE:
        E += 1
    elif bokstav == bokstavK:
        K += 1

print(f"a: {A}, e: {E}, k: {K}")
