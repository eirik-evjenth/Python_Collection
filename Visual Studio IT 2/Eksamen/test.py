class Player:
    def __init__(self, navn: str, points: int):
        self.navn = navn
        self.points = points

    def __str__(self):
        return f"{self.navn} scoret {self.points} poeng!"

    def get_pts(self):
        print(f"poeng: {self.points}")

    def set_pts(self, points):
        self.points = points

class Center(Player):
    def __init__(self, navn, points, rebounds):
        super().__init__(navn, points)
        self.rebounds = rebounds

    def __str__(self):
        return f"{self.navn} scoret {self.points} poeng og {self.rebounds} rebounds!"
    
    def get_TRB(self):
        print(f"{self.navn} rebounds: {self.rebounds}")

    def set_TRB(self, rebounds):
        self.rebounds = rebounds


Olve = Player("Olve", 23)

print(Olve)

Olve.get_pts()

Olve.set_pts(35)

Olve.get_pts()


Andreas = Center("Andreas", 55, 42)

Andreas.get_TRB()
Andreas.get_pts()


spillere = [Andreas, Olve]

for spiller in spillere:
    print(spiller)