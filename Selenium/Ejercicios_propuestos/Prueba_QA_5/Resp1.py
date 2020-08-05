class resp1:
    url = ''
    marca = ''

    def __init__(self, periodicos):
        self.periodico = periodicos
        self.marca = 'Marca'

    def setMarca(self, news):
        self.marca = news

    def obtUrl(self):
        for c, v in self.periodico.items():
            if c == self.marca:
                print(v)
                self.url = v
