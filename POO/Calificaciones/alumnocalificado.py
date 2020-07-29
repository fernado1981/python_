class calificaciones:
    califica = ["A", "B", "C", "D", "E"]
    Asignaturas = ["Matematicas", "Lengua", "Ingles", "Historia", "Fisica", "Quimica"]
    Alumno = ''
    dic = {}

    def __init__(self, alumno):
        self.Alumno = alumno
        self.media = 0
        self.count = 0
        self.contador = 0

    def setAlumno(self):
        self.Alumno = input("Alumno: ")

    def notas(self):
        self.dic[self.Alumno] = {"matematicas": int(input('Matematicas nota: ')), "Lengua": int(input('Lengua nota: ')),
                                 "Ingles": int(input('Ingles nota: ')),
                                 "Historia": int(input('Historia nota: ')), "Fisica": int(input('Fisica nota: ')),
                                 "quimica": int(input('Quimica nota: '))}

    def vernotas(self):
        for c, v in self.dic.items():
            for c, v in self.dic[c].items():
                self.count = self.count + v
                self.contador = self.contador + 1

        self.dic[self.Alumno]['sumaTotal'] = self.count
        self.dic[self.Alumno]['total'] = self.contador

    def medias(self):
        self.media = self.dic[self.Alumno]['sumaTotal'] / self.dic[self.Alumno]['total']
        if self.media < 5:
            print(self.media)
            print(self.califica[-1])
        elif self.media == 5:
            print(self.media)
            print(self.califica[-2])
        elif self.media == 6:
            print(self.media)
            print(self.califica[-3])
        elif 7 <= self.media <= 8:
            print(self.media)
            print(self.califica[-4])
        elif 9 <= self.media <= 10:
            print(self.media)
            print(self.califica[0])
        else:
            print("Fuera de limite")
