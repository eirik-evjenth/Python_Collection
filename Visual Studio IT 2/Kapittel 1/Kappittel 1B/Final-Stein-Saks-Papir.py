import random as rnd

Choices = ["st", "sa", "pa"]
W = "Du vant!"
L = "Du tapte..."
D = "Det ble uavgjort, la oss spille igjen"
U = "Ugyldig valg"
V = "Velg stein, saks, eller papir: "
Win = "Du vant mot Datamaksinen!!!"
Loss = "Du tapte mot datamaskinen..."
Start = "Vil du spille stein saks papir? 1 = ja, 2 = nei: "
trist = "Awww, forhåpentligvis neste gang"
happy = "Ok, la oss spille"

dpoeng = 0
spoeng = 0

Please = int(input(Start))

if Please == 2:
    print(trist)

elif Please == 1:
    print(happy)

    while spoeng < 3 and dpoeng < 3:
         print(f"Deg: {spoeng}   Meg: {dpoeng}")
         TilfeldigVal = rnd.choice(Choices)
         Valg = input(V)
         Valg = Valg.lower()[0:2:1]

         if Valg not in [Choices]:
             print(U)
  
         if TilfeldigVal == Valg:
             print(D)

         elif Valg == "st":
             if TilfeldigVal == "sa":
                 print(W)
                 spoeng += 1
             else:
                 print(L)
                 dpoeng += 1
    
         elif Valg == "sa":
             if TilfeldigVal == "st":
                 print(L)
                 dpoeng += 1
             else:
                 print(W)
                 spoeng += 1

         elif Valg == "pa":
             if TilfeldigVal == "st":
                 print(W)
                 spoeng += 1
             else:
                 print(L)
                 dpoeng += 1

if spoeng >= dpoeng:
    print(Win)
else:
    print(Loss)