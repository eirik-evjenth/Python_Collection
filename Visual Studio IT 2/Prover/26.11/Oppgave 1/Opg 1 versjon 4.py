# 1d

print("BMI-kalkulator")
true = False


while not true:
    vekt = input("Skriv in hvor mye du veier i kg: ")
    høyde = input("Skriv hvor høy du er i cm: ")

    try:
        vekt = float(vekt)
        høyde = float(høyde)
        høyde = høyde / 100
        BMI = vekt/(høyde*høyde)
        print(f"BMI: {round(BMI,1)}")
        break
    except ValueError:
        print("Ugyldig tall, prøv igjen")

print("Takk for nå.")
