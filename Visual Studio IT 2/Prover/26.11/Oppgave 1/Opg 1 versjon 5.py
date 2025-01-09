# 1e

print("BMI-kalkulator")

true = False


while not true:
    vekt = input("Skriv in hvor mye du veier i kg: ")
    høyde = input("Skriv hvor høy du er i cm: ")

    try:
        vekt = float(vekt)
        høyde = float(høyde)
        høyde /= 100

        BMI = vekt/(høyde*høyde)

        if BMI <= 18.4:
            kategori = "(Undervektig)"
        elif BMI <= 24.9:
            kategori = "(Normalvektig)"
        elif BMI > 25:                   #Kan sette "else", men er mer oversiktlig som dette
            kategori = "(Overvektig)"

        print(f"BMI: {round(BMI,1)} {kategori}")
        break

    except ValueError:
        print("Ugyldig tall, prøv igjen")

print("Takk for nå.")



# 1f

'''
Hvis man skriver inn negative tall så merker ikke programmet det og gir ut et negativt BMI, 
det er ikke mulig å ha negativ vekt, så programmet burde merke det.

Hvis man har en "Keyboard Interrupt" så bare stopper programmet og ser ut som en feilmelding
Så kan bare ha noe som sier at det skjedde slik at brukeren er bevisst på det.

Hvis brukeren skriver relativt normalt, så fungerer det ganske fint og gir forventet resultat
'''