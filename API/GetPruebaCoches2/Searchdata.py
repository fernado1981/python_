import requests


class Searchdata:
    response = ''
    lista = []
    count = 1
    color = ''
    matriculaColor = {}

    # inicializamos la variables necesarias con los datos pasados al contructor
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.color = 'red'

    def setColor(self, color):
        self.color = color

    # Método de busqueda
    def searchApiGet(self):
        # peticion get a la url dada
        self.response = requests.get(self.url)
        # se imprime el status
        print(self.response.status_code)

        # se transforman los datosa obtenidos a json
        self.response = self.response.json()
        # se añaden a la lista
        self.lista.append(self.response)

        # recorremos el array por posición
        for i in range(len(self.lista)):
            # recorremos las listas del array por clave valor
            for c, v in self.lista[i].items():
                if c == self.data:
                    for c, v in self.lista[i][c].items():
                        if type(v) == dict:
                            for c, v in v.items():
                                if self.color in v:
                                    self.matriculaColor[c] = {self.color: {'vehículos': v.count(self.color)}}
                                    self.count += 1
                                else:
                                    pass
                        else:
                            pass
                else:
                    pass

    def showdisponibilitycars(self):
        print("total cohes disponibles con el color", self.color, ": ", self.count)
        for c, v in self.matriculaColor.items():
            print(c, v)
