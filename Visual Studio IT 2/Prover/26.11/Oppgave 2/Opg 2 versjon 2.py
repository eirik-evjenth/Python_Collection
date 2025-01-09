import time


cars = []

class Parkinglot():
    free_space = 20

    def __init__(self, cars):
        self.cars = cars

        for car in cars:
            Parkinglot.free_space -=1
            self.space = Parkinglot.free_space
            self.spots = self.space


        

class Car():

    car_count = 0

    def __init__(self, time):
        self.time = time

        Car.car_count += 1
        self.id = Car.car_count
        self.car_number = self.id


    def park(self):
        cars.append(self)

    def avgift(self):
        self.cost = (round((time.time() - self.time) / 60)) * 1.5       # Er ganske tungtlest linje, men dette finner antall sekunder 
                                                                        # siden bilen parkerte, også forandrer det til minutter og ganger 
                                                                        # med 1.5 for antall kr de må betale



green_car = Car(time.time())


green_car.park()
green_car.avgift()

bygarasjen = Parkinglot(cars)

print(bygarasjen.spots)

# print(green_car.cost)

# Nå er det en avgift or en antall plasser