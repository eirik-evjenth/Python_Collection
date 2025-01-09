import random as rnd

Choices = ["stein", "saks", "papir"]

antall_papir = 0
antall_saks = 0
antall_stein = 0
antall_kast = 0

while antall_kast < 1000000:
    choice = rnd.choice(Choices)
    antall_kast += 1
    if choice == "stein":
        antall_stein += 1

    elif choice == "papir":
        antall_papir += 1

    else:
        antall_saks += 1 

print(f"Etter {antall_kast} kast fikk du {antall_stein} ganger stein, {antall_saks} ganger saks og {antall_papir} ganger papir.")