
def tall_liste():

    tall = []
    delt_tall = []

    lengde = int(input("Hvor mange tall vil du ha i listen?: "))
    runder = 0
    while True:

        if runder >= lengde:
            end = int(input("Vil du legge til flere verdier? 1 for ja, 2 for nei: "))
            if end == 2:
                break

            elif end != 1 and end != 2:
                print("Ugyldig valg! Vi stopper her.")
                break

            else:
                mer = int(input("Hvor mange mer tall vil du ta i listen?: "))
                lengde += mer
                
        tall_addisjon = int(input("Skriv inn et tall du vil skal gå i listen: "))
        tall.append(tall_addisjon)
        runder += 1



    tall_deler = int(input("Skriv inn et tall du vil listen skal deles med: "))

    for numbers in tall:
        if numbers % tall_deler == 0:
            delt_tall.append(numbers)

    return print(delt_tall)

tall_liste()
