import time

class Parkeringshus():
    def __init__(self, antall_biler):
        self.antall_biler = antall_biler

class Bil():

    bil_count = 0

    def __init__(self, time):


        self.time = time

        Bil.bil_count += 1
        self.id = Bil.bil_count
        self.bil_number = self.id

green_car = Bil(time.time())

print(f"The green car has the id: {green_car.id}")
print(f"The green car enters the parking lot at: {green_car.time}")


# Oppretter noen generelle klasser og ser at det fungerer