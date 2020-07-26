class profesor:
    limit = 3

    def __init__(self, alumnado, name):
        self.alumnos = alumnado
        self.name = name

    def aprobar(self):
        if self.name in self.alumnos:
            for c, v in self.alumnos.items():
                if c == self.name:
                    v['aprobar'] = True


    def suspender(self):
        for c, v in self.alumnos.items():
            if c == self.name:
                v['aprobar'] = False


    def amonestaciones(self, num):
        for c, v in self.alumnos.items():
            if c == self.name:
                v['amonestaciones'] = num
                if v['amonestaciones'] >= self.limit:
                    self.suspender()


    def desamonestar(self, num):
        for c, v in self.alumnos.items():
            if c == self.name:
                v['amonestaciones'] -= num
                if v['amonestaciones'] < 3:
                    v['aprobar'] = True


    def verAlumnado(self):
        for c,v in self.alumnos.items():
            print(c, v)

    def suspensos(self):
        for c,v in self.alumnos.items():
            if not v['aprobar']:
                print(c,v)

    def aprobados(self):
        for c, v in self.alumnos.items():
            if v['aprobar']:
                print(c, v)
