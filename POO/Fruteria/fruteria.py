class fruteria:
    comercio = {"platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    fruta = ''
    kilos = 0

    def __init__(self, f, k):
        self.fruta = f
        self.kilos = k

    def comprarFruta(self):
        while True:
            if self.fruta in self.comercio:
                print("su precio es de :", self.comercio[self.fruta] * self.kilos)
                break
            else:
                print("Lo sentimos mucho no tenemos esa fruta\nNuestra fruta:")
                for c,v in self.comercio.items():
                    print(c)

            self.fruta = input("que fruta desea: ")
            self.kilos = float(input("¿cuantos kilos: "))

        for c, v in self.comercio.items():
            if self.fruta in c:
                print("su fruta: ", c, ' su precio ', v * self.kilos)
                break
            else:
                pass