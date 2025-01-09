# 1b

print("BMI-kalkulator")

vekt = float(input("Skriv in hvor mye du veier i kg: "))
høyde = float(input("Skriv hvor høy du er i cm: "))

høyde /= 100
BMI = vekt/(høyde*høyde)

print(f"BMI: {round(BMI,1)}")