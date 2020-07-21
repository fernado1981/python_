from os import remove

import requests


class Searchdata:
    url = ''
    responseJson = ''
    response = ''
    data = ''
    lista = []

    def __init__(self, url, data):
        self.url = url
        self.data = data

    def searchApiGet(self):
        self.response = requests.get(self.url)
        print(self.response.status_code)

        self.responseJson = self.response.json()
        self.lista.append(self.responseJson)

        for i in range(len(self.lista)):
            print(self.lista[i])
            for c, v in self.lista[i].items():
                print(c, v)
                if c == self.data:
                    self.lista[i] = c
                    if len(self.lista) >= 1:
                        print(self.lista)
        print(self.lista)
