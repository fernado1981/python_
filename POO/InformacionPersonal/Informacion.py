class Informacion:
    informacion = {}
    datos = []

    def __init__(self, dato):
        self.datos = dato

    def agregarInfo(self):
        for i in range(len(self.datos)):
            self.informacion[self.datos[i]] = input(self.datos[i])
            print(self.informacion)
