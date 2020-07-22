from os import remove

import requests


class Searchdata:
    url = ''
    responseJson = ''
    response = ''
    data = ''
    lista = []
    
    #inicializamos la variables necesarias con los datos pasados al contructor
    def __init__(self, url, data):
        self.url = url
        self.data = data

     #Método de busqueda
    def searchApiGet(self):
        #petició
    def searchApiGet(self):
        #peticion get a la url dada
        self.response = requests.get(self.url)
        #se imprime el status
        print(self.response.status_code)
        
        #se transforman los datosa obtenidos a json 
        self.responseJson = self.response.json()
        #se añaden a la lista
        self.lista.append(self.responseJson)

        #recorremos el array por posición
        for i in range(len(self.lista)):
            #recorremos las listas del array por clave valor
            for c, v in self.lista[i].items():
                #buscamos si coincide la clave con el elemento a buscar
                if c == self.data:
                    #si coincide lo metemos en la lista en la posicion de i
                    self.lista[i] = c
                    #comprobamos que no este vacia la lista
                    if len(self.lista) >= 1:
                        #imprimimos la lista
                        print(self.lista)
        print(self.lista)
