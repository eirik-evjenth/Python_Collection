def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et tall.")

def get_int(prompt, valid_options):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_options:
                return value
            else:
                print(f"Vennligst velg et av følgende alternativer: {valid_options}")
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et tall.")

a = get_int("Velg 1, 2 eller 3 for fullstendig uelastisk, uelastisk, eller elastisk støt: ", [1, 2, 3])
m1 = get_float("Hva er massen til legeme nr 1?: ")
v1 = get_float("Hva er farten til legeme nr 1 før støtet?: ")
m2 = get_float("Hva er massen til legeme nr 2?: ")
v2 = get_float("Hva er farten til legeme nr 2 før støtet?: ")

if a == 1:
    u = (m1 * v1 + m2 * v2) / (m1 + m2)
    print(f"Farten til den samlede massen etter støtet er {round(u, 2)} m/s.")
    
elif a == 2:
    b = get_int("Hvilket legemet vet du farten til etter støtet? (1 eller 2): ", [1, 2])

    if b == 1:
        u1 = get_float("Hva er farten til legeme nr 1 etter støtet?: ")
        u2 = (m1 * v1 + m2 * v2 - m1 * u1) / m2
        print(f"Farten til legeme nr 2 etter støtet er {round(u2, 2)} m/s.")

    else:
        u2 = get_float("Hva er farten til legeme nr 2 etter støtet?: ")
        u1 = (m1 * v1 + m2 * v2 - m2 * u2) / m1
        print(f"Farten til legeme nr 1 etter støtet er {round(u1, 2)} m/s.")

else:
    u1 = (m1 * v1 - m2 * v1 + 2 * m2 * v2) / (m1 + m2)
    u2 = (2 * m1 * v1 - m1 * v2 + m2 * v2) / (m1 + m2)
    print(f"Farten til legeme nr 1 etter støtet er {round(u1, 2)} m/s.")
    print(f"Farten til legeme nr 2 etter støtet er {round(u2, 2)} m/s.")