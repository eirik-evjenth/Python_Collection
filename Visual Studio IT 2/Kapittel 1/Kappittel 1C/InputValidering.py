true = False

try:
    while not true:
        tall = input("Skriv inn et heltall: ")

        try:
            tall = int(tall)
            if tall > 0:
                true = True
            else:
                print("Tallet er mindre enn 0")
            true = True
        except ValueError:
            print("Ugyldig valg, prøv igjen")
except KeyboardInterrupt:
    print()
    print("Takk for nå")
    
print(f"Du skrev {tall}")