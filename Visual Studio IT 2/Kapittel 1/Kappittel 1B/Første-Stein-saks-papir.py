import random as rnd
W = "Du vant!"
L = "Du tapte..."
D = "Det ble uavgjort, la oss spille igjen"
U = "Ugyldig valg"

TilfeldigVal = rnd.choice(["st", "sa", "pa"])
Please = int(input("Vil du spille stein saks papir? 1 = ja, 2 = nei: "))
if Please == 2:
    print("Awww, forhåpentligvis neste gang")
elif Please == 1:
    print("Ok, la oss spille")
    Valg = input("Velg en av stein, saks, eller papir: ")
    True_Valg = Valg.lower()[:2]
    if TilfeldigVal == True_Valg:
        print(D)
        Ny_Valg = input("Velg en ny av stein, saks, eller papir: ")
        True_Ny_Valg = Valg.lower()[:2]
        Ny_TilfeldigVal = rnd.choice(["st", "sa", "pa"])
        if True_Ny_Valg == TilfeldigVal:
            print("Det ble uavgjort igjen, jeg mistenker det for juks og vil ikke spille.")
        elif Ny_TilfeldigVal == "st" and True_Valg == "pa":
             print(W)
        elif Ny_TilfeldigVal == "st" and True_Valg == "sa":
             print(L)
        elif Ny_TilfeldigVal == "pa" and True_Valg == "sa":
              print(W)
        elif Ny_TilfeldigVal == "pa" and True_Valg == "st":
             print(L)
        elif Ny_TilfeldigVal == "sa" and True_Valg == "st":
              print(W)
        elif Ny_TilfeldigVal == "sa" and True_Valg == "pa":
             print(L)
        else:
             print(U)
    elif TilfeldigVal == "st" and True_Valg == "pa":
        print(W)
    elif TilfeldigVal == "st" and True_Valg == "sa":
        print(L)
    elif TilfeldigVal == "pa" and True_Valg == "sa":
        print(W)
    elif TilfeldigVal == "pa" and True_Valg == "st":
        print(L)
    elif TilfeldigVal == "sa" and True_Valg == "st":
        print(W)
    elif TilfeldigVal == "sa" and True_Valg == "pa":
        print(L)
    else:
      print(U)
else:
    print(U)