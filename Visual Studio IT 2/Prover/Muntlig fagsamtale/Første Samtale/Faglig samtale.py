## sensor
## høytale, temp

import random as rnd
import datetime as dt

class Sensor():
    def __init__(self, navn, plassering):
        self.navn = navn
        self.plassering = plassering


    def get_mål(self):
        pass # Gjør noe for å få inn data

class Temperatur(Sensor):
    def __init__(self, navn, plassering):
        super().__init__(navn, plassering)

    def get_temp(self):
        return rnd.randint(1,10)




temp_sensor = Temperatur("temp sensor", "kjøkkenet")

print(temp_sensor.get_temp())



class Objekt():
    '''


tid_på_dag = dt."finn tid på dag"

class Smarthus():
    '''