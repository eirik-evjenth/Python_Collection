# Baseklasse
class Person:
    def __init__(self, navn):
        self.navn = navn

    def __str__(self):
        return f"{self.__class__.__name__}: {self.navn}"

# Elevklasse
class Elev(Person):
    def __init__(self, navn):
        super().__init__(navn)
        self.kunnskap = []  # Liste over fag eleven har lært

    def lær(self, fag):
        if fag not in self.kunnskap:
            self.kunnskap.append(fag)
            print(f"{self.navn} har lært {fag}.")
        else:
            print(f"{self.navn} kan allerede {fag}.")

    def vis_kunnskap(self):
        print(f"{self.navn} har lært: {', '.join(self.kunnskap)}")

# Lærerklasse
class Lærer(Person):
    def __init__(self, navn, fagområde):
        super().__init__(navn)
        self.fagområde = fagområde

    def undervis(self, elev, fag):
        print(f"{self.navn} underviser {elev.navn} i {fag}.")
        elev.lær(fag)

# Eksempel på bruk
elev1 = Elev("Sara")
lærer1 = Lærer("Martin", "Matematikk")

lærer1.undervis(elev1, "Python")
lærer1.undervis(elev1, "Algoritmer")

elev1.vis_kunnskap()