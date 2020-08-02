from pip._vendor import requests


class suspicious:
    lista = []

    def __init__(self, api):
        self.url = api

    def getdata(self):
        response = requests.get(self.url)
        print(response.status_code)
        response = response.json()

        self.lista.append(response)
        for i in range(len(self.lista)):
                for c,v in self.lista[i].items():
                    if c == "suspicious_car":
                        self.lista.clear()
                        self.lista.append(c)
                        self.lista.append(v)

    def showLista(self):
        for i in self.lista:
            print(i)

