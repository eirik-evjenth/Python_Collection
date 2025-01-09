tall = [3, 4, 1, 2, 5]

holdeverdi1 = tall[0]
tall[0] = tall[2]
tall[2] = holdeverdi1

holdeverdi2 = tall[1]
tall[1] = tall[3]
tall[3] = holdeverdi2

print(tall)