import time
import datetime as dt


cars = []



class Car():

    car_count = 0

    def __init__(self, name,time, license_plate, color):
        self.name = name
        self.time = time
        self.license_plate = license_plate
        self.color = color

        Car.car_count += 1
        self.id = Car.car_count
        self.car_number = self.id


    def park(self):
        cars.append(self)
        print(f"A new car, {self.name}, has parked in the parkinglot at {self.time}")
        print(f"The {self.name} has the license plate: {self.license_plate}")
        print()

    def leave(self):
        current_time = time.time()
        parking_time = time.mktime(self.time.timetuple())   # https://www.geeksforgeeks.org/how-to-convert-datetime-to-unix-timestamp-in-python/
        time_difference = current_time - parking_time
        minute_difference = round(time_difference // 60)
        self.cost = minute_difference * 1.5   
        print(f"{self.name} had to pay {self.cost} kr after {minute_difference} minutes in the parkinglot") 
        print(f"{self.license_plate}, {self.color}, {self.name} left the parkinglot")
        cars.remove(self)




class Parkinglot():
    free_space = 20

    def __init__(self, cars):
        self.cars = cars

        for car in cars:
            Parkinglot.free_space -= 1
            self.space = Parkinglot.free_space
            self.spots = self.space

    def show_color(self, color, cars):
        print(f"parked cars that are {color}:")
        for car in cars:
            if car.color == "white":    
                print(car.name)


bygarasjen = Parkinglot(cars)




Tesla_X = Car("Tesla X", dt.datetime(2024, 11, 26, 10, 45), "EV 123456", "white")
Tesla_Y = Car("Tesla Y", dt.datetime(2024, 11, 26, 11, 30), "EE 98765", "white")
Tesla_S = Car("Tesla S", dt.datetime(2024, 11, 26, 12, 45), "ZZ 24801","blue")
Tesla_Cybertruck = Car("Tesla Cybertruck", dt.datetime(2024, 11, 26, 17, 19),"SV 42791" ,"red")
Tesla = Car("Tesla", dt.datetime(2024, 11, 26, 14, 23), "EL 12978","black")



Tesla_X.park()
Tesla_Y.park()
Tesla.park()


'''                 #Gjorde litt testing, ser ut at man kan parkere en bil, finne avgiften også fjerne bilen.
red_car.park()       Det var i fortiden så noen ting stemmer ikke lenger, f.eks navnene
yellow_car.park()

for car in cars:
    car.avgift()

for car in cars:
    print(f"{car.cost}")

print(cars)

for car in cars:
    car.leave()
'''


bygarasjen.show_color("white", cars)   # Endelig klarte å finne fargene

Tesla_Y.leave()

'''
for car in bygarasjen.cars:
    if car.color == "white":
        print(car)
'''


'''
Her skal jeg skrive det jeg har klart for oversikt:

1. Når en bil kjører inn i parkeringshuset, eller når funksjonen "park" skjer med en bil, så
   går den i en liste med biler i parkeringshuset, navn og tidspunkt registreres og skrives ut.

2.  Når en bil kjører ut av parkeringshuset, leave funksjonen, så beregnes avgiften fra den kom inn,
    den betaler en antall kroner, se matten jeg gjorde, også økes ledige plassene med 1, siden 
    listen med biler minker, problemet mitt er at jeg klarer ikke å skrive ut antall ledige plasser,
    skal rydde for versjon 4 og se om jeg klarer å løse det

3.  Jeg har gjort det mulig å skrive ut alle biler med en viss farge

4. Det siste som jeg har ikke gjort er lage og håndtere et spesielt type kjøretøy, som i oppgave eksemplet "lastebil"

5. jeg har testet allerede ganske mye funksjonalit, men skal se på det mer i eksempel 4.

'''