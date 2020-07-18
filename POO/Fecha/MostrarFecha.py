class MostrarFecha:
    fechaDic = {}
    fecha = []

    def __init__(self, date):
        self.fecha = date

    def cambioFecha(self):
        self.fechaDic['dia'] = self.fecha[0]
        self.fechaDic['mes'] = self.fecha[1]
        self.fechaDic['año'] = self.fecha[2]
        print(self.fechaDic)
        print("dia: ", self.fechaDic['dia'], ' mes: ', self.fechaDic['mes'], ' año: ', self.fechaDic['año'])
