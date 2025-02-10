mol_h = float(input("Hvor mange mol er det på høyre side?: "))
mol_v = float(input("Hvor mange mol er det på venstre side?: "))
delta_H = float(input("Skriv inn entalpiendringen i kJ: "))

if mol_h > mol_v: # Hvis mere mol på høyre side så vil senking av trykk øke mengde produkter
    print("Senk trykket, likevekten skyves mot høyre")
elif mol_v > mol_h:
    print("Øk trykket, likevekten skyves mot høyre")
elif mol_h == mol_v:
    print("Trykk har ingen påvirkning")

if delta_H > 0:
    print("Øk temperaturen for mer produkter, likevekten forskyves mot høyre")
elif delta_H < 0:
    print("Senk temperaturen, likevekten forskyves mot høyre")
