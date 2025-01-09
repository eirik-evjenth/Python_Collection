Liter = float(input("Hvor mange liter vil du omgjøre til desiliter (bruk desimaltall): "))
Desiliter = Liter * 10

Temperatur_F = float(input("Skriv en temperatur i fahrenheit du vil se i celsius: "))
Temperatur_C = (Temperatur_F - 32) * 5 / 9 

Tid = float(input("Hvor mange minutter vil du forkorte til timer og minutter?: "))
Timer = Tid // 60
Minutter = Tid % 60


print(f"{Liter} liter tilsvarer {Desiliter} desiliter")
print(f"{Temperatur_F} F i celsius er {Temperatur_C} C")
print(f"{Tid} minutter er {Timer} timer og {Minutter} minutter.")