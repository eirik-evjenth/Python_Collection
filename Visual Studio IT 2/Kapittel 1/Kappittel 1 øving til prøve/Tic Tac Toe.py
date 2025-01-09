import random as rnd

spillområdeHorisontal = { 
    "1": "------------",
    "2": "------------",
}

spillerområdeVertikal = {
    "1": "   |    |   ",
    "2": "   |    |   ",
    "3": "   |    |   "
}

def print_breatt():

    # Lager spilleområdet
    
    spillområdeHorisontal = { 
    "1": "------------",
    "2": "------------",
}

spillerområdeVertikal = {
    "1": "   |    |   ",
    "2": "   |    |   ",
    "3": "   |    |   "
}

print(spillerområdeVertikal["1"])
for verdier in spillområdeHorisontal:
    print(spillområdeHorisontal[verdier])
    print(spillerområdeVertikal[verdier])
    
while True:
    pass

print(TicTacToe())
