# Ordbok med definisjoner
Ordbok = {
    "variabel": "Et symbol som lagrer en verdi i et program.",
    "datatype": "Definerer hvilken type data en variabel kan inneholde, f.eks. heltall (int), flyttall (float), tekst (str).",
    "operator": "Et symbol som utfører en operasjon på en eller flere verdier, f.eks. + (pluss), - (minus), * (multiplikasjon).",
    "løkke": "En kodeblokk som gjentas flere ganger, f.eks. for-løkke eller while-løkke."
}

# Funksjon som lar brukeren velge et ord og få definisjonen
def vis_definisjon():
    while True:
        print("\nVelg et ord for å få definisjonen, eller skriv avslutt for å avslutte:")
        for words in Ordbok:
            print(f"- {words}")
        
        valg = input("\nSkriv ordet du vil ha definisjonen for: ").lower()
        
        if valg == "avslutt":
            print("Avslutter programmet...")
            break
        elif valg in Ordbok:
            print(f"\nDefinisjon av '{valg}': {Ordbok[valg]}")
        else:
            print("\nUgyldig valg, prøv igjen.")

# Kjører funksjonen
vis_definisjon()
print()