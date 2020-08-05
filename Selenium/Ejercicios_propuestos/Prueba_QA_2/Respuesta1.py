class Respuesta1:
    marca = ''

    def __init__(self, periodicos):
        self.periodico = periodicos
        self.marca = 'Marca'

    def setmarca(self, news):
        self.marca = news

    def obtMarca(self):
        for c,v in self.periodico.items():
            if c == self.marca:
                url=v
                print(v)