'''
class Temperatur:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self, verdi):
        self._celsius = (verdi - 32) / 1.8

t = Temperatur(0)
print(t.fahrenheit)  # 32.0

t.fahrenheit = 212
print(t._celsius)    # 100.0
'''

class Rektangel:
    def __init__(self, høyde, bredde):
        self.høyde = høyde
        self.bredde = bredde

    @property
    def areal(self):
        return self.høyde * self.bredde

figur1 = Rektangel(10,15)

print(figur1.areal)