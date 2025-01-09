
True_Valg = input("Skriv noe: ")
Choices = ["st", "sa", "pa"]
if True_Valg == Choices:
    print("YESS")
else:
    print("sad")

tall1 = float(input("Hva skal første tallet være? "))
tall2 = float(input("Hva skal andre tallet være? "))
resultat = tall1 + tall2

print(f"Summen av {tall1} og {tall2} er {resultat}")

Papir = input("Skriv papir: ")
Valg = Papir.lower()[:2]

print(Valg)
