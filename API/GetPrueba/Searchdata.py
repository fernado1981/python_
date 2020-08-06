import requests


class Searchdata:
    url = ''
    responseJson = ''
    response = ''
    data = ''
    lista = []
    listaA = []

    # inicializamos la variables necesarias con los datos pasados al contructor
    def __init__(self, url, data):
        self.url = url
        self.data = data

    # Método de busqueda
    def searchApiGet(self):
        # peticion get a la url dada
        self.response = requests.get(self.url)
        # se imprime el status
        print(self.response.status_code)

        # se transforman los datosa obtenidos a json
        self.responseJson = self.response.json()
        # se añaden a la lista
        self.lista.append(self.responseJson)

        # recorremos el array por posición
        for i in range(len(self.lista)):
            # recorremos las listas del array por clave valor
            for c, v in self.lista[i].items():
                if c == self.data:
                    for c, v in self.lista[i][c].items():
                        if type(v) == dict:
                            for c, v in v.items():
                               print(c, v)


                # buscamos si coincide la clave con el elemento a buscar
                #if c == self.data:
                    # si coincide lo metemos en la lista en la posicion de i
                 #   self.listaA.append(c)
                 #   self.listaA.append(v)
                #else:
                 #   pass
       # print(self.listaA)
