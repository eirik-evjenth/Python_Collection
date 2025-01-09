Tall = float(input("Skirv inn et tall blud: "))

if Tall != 0:
    if Tall > 0:
        if Tall >= 100:
            print("tallet er større enn 100")
        else: 
            print("Tallet er positiv mindre enn 100")
    else:
        if Tall <= -100:
            print("Tallet er mindre enn -100")
        else:
            print("Tallet er negativ større enn -100")
else:
    print(f"Tallet er 0")