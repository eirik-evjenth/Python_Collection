class Spiller:
    def __init__(self, navn: str, poeng: int):
        self.navn = navn # _Spiller__navn
        self.poeng = poeng



    def get_pts(self):
        print(self.poeng)

    def set_pts(self, poeng):
        self.poeng = poeng


    def info(self):
        print(f"{self.navn} har scoret {self.poeng} poeng")


class Center(Spiller):
    def __init__(self, navn: str, poeng: int, rebounds: int, blocks: int):
        super().__init__(navn, poeng)
        self.rebounds = rebounds
        self.blocks = blocks

    def info(self):
        print(f"{self.navn} har scoret {self.poeng} poeng, {self.rebounds} rebounds")
    

andreas = Spiller("Andreas", 22)

olve = Center("Olve", 19, 12, 2)

spillere = [olve, andreas]

for spiller in spillere:
    spiller.info()
