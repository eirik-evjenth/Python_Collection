
def BMI_kalkulator(vekt: int, høyde: int):
    BMI = vekt/høyde**2
    if BMI < 18.5:
        return "Undervekt"
    elif BMI < 25:
        return "Normal vekt"
    elif BMI < 30:
        return "Overvektig"
    elif BMI < 35:
        return "Fedme, grad 1"
    elif BMI < 40:
        return "Fedme, grad 2"
    elif BMI >= 40:
        return "Fedme, grad 3"