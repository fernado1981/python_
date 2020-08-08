import requests


class Searchdata:
    response = ''
    lista = []
    listaOrder = []

    # inicializamos la variables necesarias con los datos pasados al contructor
    def __init__(self, url, data, Matricula, Intervalo):
        self.url = url
        self.data = data
        self.Matricula = Matricula
        self.Intervalo = Intervalo

    # Método de busqueda
    def searchApiGet(self):
        self.response = requests.get(self.url)
        print(self.response.status_code)

        self.response = self.response.json()
        self.lista.append(self.response)

        for i in self.lista:
            for c, v in i.items():
                if type(v) == dict:
                    for c, v in v.items():
                        if self.Matricula in v:
                            for c, v in v.items():
                                self.listaOrder.append(c)
                                print(self.listaOrder)
                        else:
                            pass
                else:
                    pass

    def showIntervalo(self):
        for i in range(len(self.listaOrder)):
            if self.Intervalo in self.listaOrder[i]:
                del self.listaOrder[i+1:]
                break

        print(self.listaOrder)
