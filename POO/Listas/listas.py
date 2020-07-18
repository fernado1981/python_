class listas:
    asignaturas = []
    loteria = []
    numeros = []
    pos = []
    word = []
    vocales=[]
    dicNotaAsignatura = {}
    count = 0
    countAprobado = 0
    countSuspenso = 0
    countA = 0
    countB = 0

    def __init__(self, asignatura,vocal):
        self.asignaturas = asignatura
        self.vocales = vocal

    def estudio(self):
        for i in self.asignaturas:
            print("yo estudio: ", i)

    def nota(self):
        for i in range(len(self.asignaturas)):
            print(self.asignaturas[i])
            nota = int(input("Nota: "))
            self.dicNotaAsignatura[self.asignaturas[i]] = nota

        for self.asignatura, nota in self.dicNotaAsignatura.items():
            if nota >= 5:
                print("has aprobado las siguientes asignaturas: ", self.asignatura, ' con ', nota)
            else:
                print("has suspendido las siguientes asignaturas: ", self.asignatura, ' con ', nota)

        for i in self.dicNotaAsignatura:
            if self.dicNotaAsignatura[i] >= 5:
                self.countAprobado += 1
                self.countA = self.countA + self.dicNotaAsignatura[i]

            else:
                self.countSuspenso += 1
                self.countB = self.countB + self.dicNotaAsignatura[i]

        print(self.dicNotaAsignatura)
        print("has aprobado: ", self.countAprobado)
        print("Has supendido: ", self.countSuspenso)
        print("la nota media es de :", (self.countA + self.countB) / len(self.asignaturas))

    def numLoteria(self):
        for i in range(5):
            num = int(input("Dame numero: "))
            self.loteria.append(num)
            self.loteria.sort()
        print("los numeros de la lotería son: ", self.loteria)

    def invertirNum(self):
        for i in range(10):
            num = int(input("Dame numero: "))
            self.numeros.append(num)

        self.numeros.sort(reverse=True)
        print(self.numeros)

    def delAsignaturePass(self):
        while self.count < len(self.asignaturas):
            asignatura = self.asignaturas[self.count]
            print(asignatura)
            nota = int(input("Dime tu nota: "))
            if nota >= 5:
                self.pos.append(self.asignaturas.index(asignatura))
            else:
                pass
            self.count += 1
            self.pos.sort(reverse=True)

        for i in range(len(self.pos)):
            position = self.pos[i]
            self.asignaturas.pop(position)
        print("Asignaturas para repetir: ", self.asignaturas)

    def vocalesrepe(self):
        palabra = input("dime una palabra: ")
        aux=0
        for i in palabra:
            self.word.append(i)
            if i in self.vocales:
                print(i, "esta repetida ", self.word.count(i), " veces")
            self.count += 1
