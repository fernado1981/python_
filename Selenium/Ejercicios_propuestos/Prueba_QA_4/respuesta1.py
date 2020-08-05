class respuesta1:
    marca = ''
    url = ''

    def __init__(self, periodico):
        self.periodicos = periodico
        self.marca = 'Marca'

    def setNew(self, param):
        self.marca = param.lower()

    def obtUrl(self):
        self.marca.lower()
        for c, v in self.periodicos.items():
            if c == self.marca:
                self.url = v
                print(v)
