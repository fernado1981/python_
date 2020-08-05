import requests


class Resp2:
    color = ''
    response = ''
    lista = []

    def __init__(self, url_Api,sospechoso):
        self.suspicious = sospechoso
        self.url = url_Api
        self.color = 'black'

    def setColor(self, colour):
        self.color = colour

    def obtData(self):
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            self.response = self.response.json()
            for c, v in self.response.items():
                if c == self.suspicious:
                    self.lista.append(c)
                    self.lista.append(v)

    def deleteColorList(self):
        for i in range(len(self.lista)):
            for x in self.lista[i]:
                if self.color in x:
                    pos = self.lista[i].index(x)
                    self.lista[i].pop(pos)

    def addlist(self, val):
        self.lista.append(val.lower())

    def showList(self):
        print(self.lista)
