class Divisas:
    divisas = {}
    moneda = []
    Divisas = []

    def __init__(self, divi, monedas):
        self.divisas = divi
        self.moneda = monedas
        self.Divisas = list(self.divisas)

    def verDivisas(self):
        for i in range(len(self.Divisas)):
            if self.Divisas[i].lower() == "euro":
                self.divisas[self.Divisas[i].lower()] = self.moneda[0]
            if self.Divisas[i].lower() == "dollar":
                self.divisas[self.Divisas[i].lower()] = self.moneda[1]
            elif self.Divisas[i].lower() == "yen":
                self.divisas[self.Divisas[i].lower()] = self.moneda[2]
            else:
                pass

        print(self.divisas)

        while True:
            divisa = input("Dime una divisa: ")
            if divisa in self.divisas:
                print("encontrada")
                print(self.divisas[divisa])
                break
            else:
                print("no tenemos dicha divisa, lo sentimos")
