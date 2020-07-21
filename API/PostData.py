from heapq import merge

import requests


class postData:
    url = ''
    data = {}
    lista = []

    def __init__(self, url, data):
        self.url = url
        self.data = data

    def AddData(self):
        print(self.data)
        response = requests.post(self.url, self.data, stream=True)
        print(response.status_code)
        response = response.json()
        self.lista.append(response)

        for i in range(len(self.lista)):
            print(i)
            print(self.lista[i]['Nombre'], '', self.lista[i]['Edad'])
