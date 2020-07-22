from heapq import merge

import requests


class postData:
    url = ''
    data = {}
    lista = []

    #generamos el constructor para inicializar las variables necesarias
    def __init__(self, url, data):
        self.url = url
        self.data = data
    
    #creamos el método para añadir el data por medio de Post
    def AddData(self):
        print(self.data)
        #generamos la petición post pasandole la url, el data y strema=True
        response = requests.post(self.url, self.data, stream=True)
        #Imprimimos el status
        print(response.status_code)
        #parseamos la respuesta a json
        response = response.json()
        #Añadimos la response a la lista
        self.lista.append(response)

        #recorremos la lista por posición
        for i in range(len(self.lista)):
            print(i)
            #imprimimos la lista para comprobar que se ha realizado correctamente
            print(self.lista[i]['Nombre'], '', self.lista[i]['Edad'])
