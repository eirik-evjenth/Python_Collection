'''Oppgave 1
Figuren nedenfor viser en bane og en syklist. Syklisten har gjennomsnittsfart 50 km/h. Lag et program som

beregner avstanden rundt banen, altså banens lengde
beregner syklistens gjennomsnittsfart i m/s
beregner tiden syklisten bruker på 10 runder
'''

import math as m

# Først skriver vi formel for omkrets rundt sirkel

r = 31.83 # m
bane_lengde = 2*m.pi*r + 200 # begge halv sirklene blir til en, og 200 m fra direkte

print(f"{round(bane_lengde, 2)} m")

forhold = 3600/1000 # Kalkulerer forholdet mellom km/t og m/s
fartKilometer = 50 # km/t
fartMeter = fartKilometer / forhold

print(f"{round(fartMeter, 2)} m/s") # ser på farten delt på forholdet

# Vi vet hva banalengden er, og han går 10 banelengder, så vet vi farten

tid = bane_lengde * 10 / fartMeter

print(f"{round(tid, 2)} s")