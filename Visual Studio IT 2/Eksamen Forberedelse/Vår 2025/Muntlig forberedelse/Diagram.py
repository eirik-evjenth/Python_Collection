import datetime as dt

class Kunde:
    def __init__(self, navn: str, epost: str):
        self.navn = navn
        self.epost = epost

    def __str__(self):
        return f"{self.navn}"

    def bestill_billett(self):
        return None

class Film:
    def __init__(self, tittel: str, varighet: int, sjanger: str):
        self.tittel = tittel
        self.varighet = varighet
        self.sjanger = sjanger

    def __str__(self):
        return f"{self.tittel}"

    def vis_info(self):
        return None

class Bestilling:
    def __init__(self, kunde: Kunde, film: Film):   # tidspunkt: object
        self.kunde = kunde
        self.film = film
        
        nå = dt.datetime.now()
        self.tidspunkt = nå.strftime("%d.%m.%Y %H:%M")


    def vis_kvittering(self):
        print(f"{self.kunde} har bestilt å se {self.film} den {self.tidspunkt}")


dune = Film("Dune", 1.5, "Space")
ola = Kunde("Ola", "ola@gmail.com")

bestilling = Bestilling(ola, dune)

bestilling.vis_kvittering()