class Bankkonto:
    def __init__(self, saldo):
        self.__saldo = saldo  # privat attributt

    def sett_inn(self, beløp):
        self.__saldo += beløp

    def ta_ut(self, beløp):
        if beløp <= self.__saldo:
            self.__saldo -= beløp
        else:
            print("Ikke nok penger på konto.")

    def vis_saldo(self):
        print(f"Du har {self.__saldo} NOK")

konto = Bankkonto()