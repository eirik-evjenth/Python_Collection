import time
import datetime as dt

class Parkinglot:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.free_spaces = total_spaces
        self.cars = []
        self.trucks = []

    def park_vehicle(self, vehicle):
        if isinstance(vehicle, Car):
            if self.free_spaces >= 1:
                self.cars.append(vehicle)
                self.free_spaces -= 1
                print(f"A new car, {vehicle.name}, has parked in the parking lot at {vehicle.time}")
                print(f"The {vehicle.name} has the license plate: {vehicle.license_plate}")
                print()
            else:
                print("No free space available for cars.")
        elif isinstance(vehicle, Truck):
            if self.free_spaces >= 2:
                self.trucks.append(vehicle)
                self.free_spaces -= 2
                print(f"A new truck, {vehicle.name}, has parked in the parking lot at {vehicle.time}")
                print(f"The {vehicle.name} has the license plate: {vehicle.license_plate}")
                print()
            else:
                print("No free space available for trucks.")

    def leave_vehicle(self, vehicle):
        current_time = time.time()
        parking_time = time.mktime(vehicle.time.timetuple())
        time_difference = current_time - parking_time
        minute_difference = round(time_difference // 60)
        
        if isinstance(vehicle, Car):
            self.cars.remove(vehicle)
            self.free_spaces += 1
            cost = minute_difference * 1.5
        elif isinstance(vehicle, Truck):
            self.trucks.remove(vehicle)
            self.free_spaces += 2
            cost = minute_difference * 3 if vehicle.height >= 3 or vehicle.length >= 7 else minute_difference * 1.5
        
        print(f"{vehicle.name} had to pay {cost} kr after {minute_difference} minutes in the parking lot")
        print(f"{vehicle.license_plate}, {vehicle.color}, {vehicle.name} left the parking lot")

    def show_color(self, color):
        print(f"Parked cars and trucks that are {color}:")
        for car in self.cars:
            if car.color == color:
                print(car.name)
        for truck in self.trucks:
            if truck.color == color:
                print(truck.name)

class Car:
    car_count = 0

    def __init__(self, name, time, license_plate, color):
        self.name = name
        self.time = time
        self.license_plate = license_plate
        self.color = color
        Car.car_count += 1
        self.id = Car.car_count

class Truck(Car):
    truck_count = 0

    def __init__(self, name, time, license_plate, color, height, length):
        super().__init__(name, time, license_plate, color)
        self.height = height
        self.length = length
        Truck.truck_count += 1
        self.id = Truck.truck_count


# Create a parking lot with 20 total spaces
bygarasjen = Parkinglot(total_spaces=20)

# Create car and truck objects with their respective attributes
Tesla_X = Car("Tesla X", dt.datetime(2024, 11, 26, 10, 45), "EV 123456", "white")
Tesla_Y = Car("Tesla Y", dt.datetime(2024, 11, 26, 11, 30), "EE 98765", "white")
Tesla_S = Car("Tesla S", dt.datetime(2024, 11, 26, 12, 45), "ZZ 24801", "blue")
Tesla = Car("Tesla", dt.datetime(2024, 11, 26, 14, 23), "EL 12978", "black")

Tesla_Cybertruck = Truck("Tesla Cybertruck", dt.datetime(2024, 11, 26, 12, 19), "SV 42791", "red", 1.8, 5.7)
Large_trailer = Truck("Large Trailer", dt.datetime(2024, 11, 26, 12, 00), "SV 42791", "red", 3.5, 12)

# Park and leave vehicles in the parking lot
bygarasjen.park_vehicle(Tesla_Cybertruck)
bygarasjen.leave_vehicle(Tesla_Cybertruck)

bygarasjen.park_vehicle(Large_trailer)
bygarasjen.leave_vehicle(Large_trailer)

# Park multiple vehicles in the parking lot
bygarasjen.park_vehicle(Large_trailer)
bygarasjen.park_vehicle(Tesla_Cybertruck)


# Show vehicles of a specific color
bygarasjen.show_color("red")

# Print the number of free spots left in the parking lot
print(f"Free spots left: {bygarasjen.free_spaces}")
