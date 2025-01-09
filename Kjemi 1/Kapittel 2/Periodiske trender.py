import matplotlib.pyplot as plt
import mendeleev as mende
import numpy as np
import chemlib as chem

# 1


atomnummer = []
elektronegativitet = []
grunnstoffer = []

try:
    while len(grunnstoffer) < 10:
        grunnstoff = input("Skriv inn et grunstoffnummer: ")
        try:
            grunnstoff = int(grunnstoff)
        except ValueError:
            print("Det må være et tall")
        if grunnstoff < 1 or grunnstoff > 118:
            print("Skriv et gyldig element")
        elif grunnstoff in grunnstoffer:
            print("Elementet er allerede lagt til")
        grunnstoffer.append(grunnstoff)
except KeyboardInterrupt:
    print("-")
    print("Du har avsluttet programmet")
    print()
    exit()

print(f"Dine utvalgte grunnstoffer: {grunnstoffer}")
print()

for grunnstoff_nummer in grunnstoffer:
    grunnstoff = mende.element(grunnstoff_nummer)
    atomnummer.append(grunnstoff.atomic_number)
    elektronegativitet_verdi = grunnstoff.electronegativity()

    if elektronegativitet_verdi is not None:
        elektronegativitet.append(elektronegativitet_verdi)
    else:
        print(f"{grunnstoff.name} har ingen definert elektronegativitet")
        print()


if len(atomnummer) == len(elektronegativitet):
    plt.figure(1)
    plt.plot(atomnummer, elektronegativitet, linestyle=" ", marker="o")
    plt.xlabel("Atomnummer")
    plt.ylabel("Elektronegativitet")
    plt.show()

else:
    print("Noen grunnstoffer har ikke elektronegativitet og ble utelatt fra plottet.")


# 2

# Det er samme program som tidligere, bare med noen utvalgte elementer

atomnummer = []
elektronegativitet = []
grunnstoffer = []

for i in range(19, 36):
    grunnstoff = mende.element(i)
    atomnummer.append(grunnstoff.atomic_number)
    elektronegativitet.append(grunnstoff.electronegativity())

for grunnstoff_nummer in grunnstoffer:
    grunnstoff = mende.element(grunnstoff_nummer)
    atomnummer.append(grunnstoff.atomic_number)
    elektronegativitet_verdi = grunnstoff.electronegativity()

    if elektronegativitet_verdi is not None:
        elektronegativitet.append(elektronegativitet_verdi)
    else:
        print(f"{grunnstoff.name} har ingen definert elektronegativitet")
        print()


if len(atomnummer) == len(elektronegativitet):
    plt.figure(1)
    plt.plot(atomnummer, elektronegativitet, linestyle=" ", marker="o")
    plt.xlabel("Atomnummer")
    plt.ylabel("Elektronegativitet")
    plt.show()

else:
    print("Noen grunnstoffer har ikke elektronegativitet og ble utelatt fra plottet.")


# 3

# 1: Definer halogener
halogener = [9, 17, 35, 53, 85]  # Atomnummer for F, Cl, Br, I, At

atomnummer = []
kokepunkt = []
grunnstoffer = []

# Validering av brukerinndata og valg
try:
    visning = input("Vil du skrive ut eller plotte kokepunktet til halogenene? (skriv/plot): ").lower()
    if visning not in ['skriv', 'plot']:
        raise ValueError("Ugyldig valg. Skriv 'skriv' eller 'plot'.")
except ValueError as e:
    print(e)
    exit()

# Hent kokepunkt for halogenene
for grunnstoff_nummer in halogener:
    grunnstoff = mende.element(grunnstoff_nummer)
    atomnummer.append(grunnstoff.atomic_number)
    kokepunkt_verdi = grunnstoff.boiling_point
    kokepunkt.append(kokepunkt_verdi)
    grunnstoffer.append(grunnstoff.name)

if visning == "skriv":
    print("Kokepunkt for halogenene:")
    for i in range(len(grunnstoffer)):
        print(f"{grunnstoffer[i]}: {kokepunkt[i]} K")
else:
    # Plotte kokepunkt
    plt.figure(1)
    plt.plot(atomnummer, kokepunkt, linestyle=" ", marker="o")
    plt.xticks(atomnummer, grunnstoffer)  # Vise navnene på halogenene
    plt.xlabel("Atomnummer")
    plt.ylabel("Kokepunkt (K)")
    plt.title("Kokepunkt for Halogener")
    plt.show()

# Forklaring av trenden i kokepunkt
print("\nTrenden i kokepunkt:")
print("Kokepunktet øker nedover i gruppen (fra fluor til astat), fordi atomene blir større og tiltrekningskreftene mellom atomene (van der Waals-krefter) øker, noe som krever mer energi for å bryte.")


# Hent atomradius for alle grunnstoffer i periodesystemet

# 4

atomnummer = []
atomradius = []

for i in range(1, 119):  # Gå gjennom alle elementene (1 til 118)
    grunnstoff = mende.element(i)
    radius_verdi = grunnstoff.atomic_radius
    # Bare legg til grunnstoffer med definert atomradius
    if radius_verdi is not None:
        atomnummer.append(grunnstoff.atomic_number)
        atomradius.append(radius_verdi)

# Plott atomradius for alle grunnstoffer
plt.figure(1)
plt.plot(atomnummer, atomradius, linestyle=" ", marker="o")
plt.xlabel("Atomnummer")
plt.ylabel("Atomradius (pm)")
plt.title("Atomradius for alle grunnstoffer")
plt.show()

# Forklaring av atomradius-trenden
print("\nTrenden i atomradius:")
print("Generelt avtar atomradius over en periode (fra venstre til høyre) på grunn av økt tiltrekning mellom elektronene og kjernen, "
      "mens den øker nedover en gruppe på grunn av nye elektronskall som legger til større avstand fra kjernen.")

# Plott atomradius for grunnstoffer 19-36
atomnummer_19_36 = []
atomradius_19_36 = []

for i in range(19, 37):  # Grunnstoff 19 til 36
    grunnstoff = mende.element(i)
    radius_verdi = grunnstoff.atomic_radius
    # Bare legg til grunnstoffer med definert atomradius
    if radius_verdi is not None:
        atomnummer_19_36.append(grunnstoff.atomic_number)
        atomradius_19_36.append(radius_verdi)

plt.figure(2)
plt.plot(atomnummer_19_36, atomradius_19_36, linestyle=" ", marker="o")
plt.xlabel("Atomnummer (19-36)")
plt.ylabel("Atomradius (pm)")
plt.title("Atomradius for grunnstoffer 19-36")
plt.show()

# Forklaring for grunnstoffer 19-36
print("\nForklaring for grunnstoffene 19-36:")
print("I dette området ser vi at atomradius generelt avtar, men det er noen unntak. Dette skyldes at elektronene fyller d-orbitalene, ")

# 5

atomnummer = []
atomradius = []
elektronegativitet = []

# Gå gjennom grunnstoffer og samle data om atomradius og elektronegativitet
for i in range(1, 119):  # Gå gjennom alle grunnstoffer fra 1 til 118
    grunnstoff = mende.element(i)
    radius_verdi = grunnstoff.atomic_radius
    elektronegativitet_verdi = grunnstoff.electronegativity()
    
    # Legg kun til grunnstoffer med både definert atomradius og elektronegativitet
    if radius_verdi is not None and elektronegativitet_verdi is not None:
        atomnummer.append(grunnstoff.atomic_number)
        atomradius.append(radius_verdi)
        elektronegativitet.append(elektronegativitet_verdi)

# Plott elektronegativitet som funksjon av atomradius
plt.figure()
plt.plot(atomradius, elektronegativitet, linestyle=" ", marker="o")
plt.xlabel("Atomradius (pm)")
plt.ylabel("Elektronegativitet")
plt.title("Elektronegativitet som funksjon av atomradius")
plt.show()

# Beskrivelse av trenden
print("\nGenerell trend:")
print("Elektronegativiteten har en tendens til å avta når atomradiusen øker. Dette skyldes at større atomer har en svakere tiltrekning til elektroner, "
      "fordi de ytre elektronene er lengre unna kjernen.")
