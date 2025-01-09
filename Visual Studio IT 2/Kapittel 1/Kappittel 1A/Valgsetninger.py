# Valgsetninger

alder = int(input("Hvor gammel er du i antall år? "))

'''
if alder < 0:
    print("Ikke lyv da")
elif alder < 12:
    print("Du er et barn")
elif alder == 12:
    print("Du er en Tween")
elif alder < 20:
    print("Du er tenåring")
elif alder == 69:
    print("Nice")
elif alder < 100:
    print("Ingenting spennende")
elif alder == 100:
    print("100!!!")
else:
    print("Du er anchient")
'''
Mopedgrense = 16
Bilgrense = 18
Bussgrense = 21

if alder < Mopedgrense:
    print("Du kan desverre ikke ta lappen")
elif alder < Bilgrense:
    print("Du kan ta lappen for motorsykkel")
elif alder < Bussgrense:
    print("Du kan ta lappen for både motorsykkel og Bil")
elif alder > 80:
    print("Jeg er usikker om du kan ta lappen, snakk til legen og se hva de synes")
else:
    print("Du kan ta hvilken som helst lap du vil")
