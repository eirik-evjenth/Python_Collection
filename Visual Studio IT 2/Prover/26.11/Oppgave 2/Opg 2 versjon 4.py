import time
import datetime as dt


cars = []
trucks = []


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

class Truck(Car):   
    truck_count = 0
    

    def __init__(self, name,time, license_plate, color, height, length):
        super().__init__(name, time, license_plate, color)
        self.height = height
        self.length = length


        Truck.truck_count += 1
        self.id = Truck.truck_count
        self.car_number = self.id


    def park(self):
        trucks.append(self)
        print(f"A new truck, {self.name}, has parked in the parkinglot at {self.time}")
        print(f"The {self.name} has the license plate: {self.license_plate}")
        print()

    def leave(self):
        current_time = time.time()
        parking_time = time.mktime(self.time.timetuple())   # https://www.geeksforgeeks.org/how-to-convert-datetime-to-unix-timestamp-in-python/
        time_difference = current_time - parking_time
        minute_difference = round(time_difference // 60)
        if self.height >= 3 or self.length >= 7:
            self.cost = minute_difference * 3
        elif self.height < 3 or self.length < 6:             # Kan ha else her, men likte det bedre med elif
            self.cost = minute_difference * 1.5
        
        print(f"{self.name} had to pay {self.cost} kr after {minute_difference} minutes in the parkinglot") 
        print(f"{self.license_plate}, {self.color}, {self.name} left the parkinglot")
        trucks.remove(self)

class Parkinglot():
    free_space = 20

    def __init__(self, cars, trucks):
        self.cars = cars
        self.trucks = trucks

        for car in cars:
            Parkinglot.free_space -= 1
            self.space = Parkinglot.free_space
            self.spots = self.space

        for truck in trucks:
            Parkinglot.free_space -= 2
            self.space = Parkinglot.free_space
            self.spots = self.space

    def show_color(self, color, cars, trucks):
        print(f"parked cars and trucks that are {color}:")
        for car in cars:
            if car.color == color:    
                print(car.name)

        for truck in trucks:
            if truck.color == color:
                print(truck.name)


bygarasjen = Parkinglot(cars, trucks)




Tesla_X = Car("Tesla X", dt.datetime(2024, 11, 26, 10, 45), "EV 123456", "white")
Tesla_Y = Car("Tesla Y", dt.datetime(2024, 11, 26, 11, 30), "EE 98765", "white")
Tesla_S = Car("Tesla S", dt.datetime(2024, 11, 26, 12, 45), "ZZ 24801","blue")
Tesla = Car("Tesla", dt.datetime(2024, 11, 26, 14, 23), "EL 12978","black")

Tesla_Cybertruck = Truck("Tesla Cybertruck", dt.datetime(2024, 11, 26, 12, 19),"SV 42791" ,"red", 1.8, 5.7) 



Tesla_Cybertruck.park()
Tesla_Cybertruck.leave() 

'''
Noe å merke seg er til og med når Tesla Cybertruck er en
"Truck" er det ikke stort nok å kreve mer penger, 
men det tar fortsatt opp mer plass enn en vanlig bil.
Nå tar vi et annet eksempel
'''

Large_trailer = Truck("Large Trailer", dt.datetime(2024, 11, 26, 12, 00),"SV 42791" ,"red", 3.5, 12) 

Large_trailer.park()
Large_trailer.leave()



'''
Her ser vi at Traileren måtte betale ekstra.
'''


Large_trailer.park()
Tesla_Cybertruck.park()
Tesla_S.park()
Tesla_X.park()

bygarasjen.show_color("red", cars, trucks)

'''
4.  For kjøretøyet "Truck" har jeg tenkt at hvis den er høyere enn 3 meter, eller lengre enn 7 så har den
    spesial behov som koster ekstra. Den tar også opp ekstra plass i parkeringshuset.

    Jeg har prøvd å gjøre alle endringene nødvendig for å har trucks og biler.

    Merker ganske sent nå at parkeringshuset har ikke selv så mye den kan gjøre, men bilene har ganske mye.
    I fremtiden må jeg være mer OBS på hva målet med koden min er
'''

'''
d)

Problemene med manuell registrering er at noen må gjøre det, det er ikke automatisk
Man må betale noen å holde øyet sitt og se på in og ut, og kan bli spesielt vanskelig hvis 
parkeringshuset er på maks kapasitet og på grunn av menneskelige feil så glemmer de,
eller gjør noe annet feil også er det biler som leter etter en plass som finnes ikke.

Vi mennesker er ikke perfekte, derfor er det mulig at feil oppstår som datamaskiner hadde klart
å unngå, derfor brukes meste parkeringshus automatisk registrering. Noe som en sensor eller annet
Hadde hjulpet veldig mye og spart tid/ ressurser på noe unødvendig.
'''