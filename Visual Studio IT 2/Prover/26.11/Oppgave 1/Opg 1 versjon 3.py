# 1c

print("BMI-kalkulator")

vekt = input("Skriv in hvor mye du veier i kg: ")
høyde = input("Skriv hvor høy du er i cm: ")

try:
    vekt = float(vekt)
    høyde = float(høyde)
    høyde /= 100
    BMI = vekt/(høyde*høyde)
    print(f"BMI: {round(BMI,1)}")
except ValueError:
    print("Du må skrive et tall for at programmet skal fungere")



