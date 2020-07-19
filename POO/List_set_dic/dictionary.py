class dictionary:
    lista = []
    dictA = {}
    dictB = {}
    clave = ''
    valor = ''

    def __init__(self, listado, dicA, dicB):
        self.dictA = dicA
        self.dictB = dicB
        self.lista = listado

    def aroundDict(self):
        # Recorre la lista y recorrer los dicionarios
        for i in range(len(self.lista)):
            for c, v in self.lista[i].items():
                if c == "jefe":
                    print(c, ':', v['Nombre'], ' ', v['Edad'])
                else:
                    print(c, ':', v['Nombre'], ' ', v['Edad'])

    def arounDictAdd(self, c, v):
        self.clave = c
        self.valor = v
        # recorrer la lista y añadir un campo al diccionario
        for i in range(len(self.lista)):
            for c, v in self.lista[i].items():
                if c == "pipiolo":
                    v[self.clave] = self.valor
                    break
        print(self.lista)

    def addkey(self):
        # añadir clave:valor al dicionariop
        self.dictA['jefe'][self.clave] = self.valor
        print(self.lista)

    def deleteBKeyValue(self, c):
        self.clave = c
        # eliminar clave:valor del dicionario
        self.dictB['pipiolo'].pop(self.clave)
        print(self.dictB)
