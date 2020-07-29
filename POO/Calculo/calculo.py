class calculo:

    def __init__(self, h, A):
        self.Alto = h
        self.Ancho = A

    def areaRectangulo(self):
        return self.Ancho*self.Alto

    def perimetroRectangulo(self):
        print("el perímetro es: ", (self.Alto + self.Ancho) * 2)

    def mayorque(self):
        if self.Alto > self.Ancho:
            print("numA es mayor que numB")
        elif self.Alto < self.Ancho:
            print("numB es mayor que numA")
        else:
            print("ambos son iguales")

