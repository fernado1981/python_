import requests

from Selenium.Ejercicios_propuestos.Prueba_QA_16.data import data


class apiGet(data):
    response = ''

    def __init__(self):
        self.data = data.dataApi

    def getData(self):
        self.response = requests.get(self.data['url'])
        if self.response.status_code == 200:
            self.response = self.response.json()

    def searchWord(self):
        for c, v in self.response.items():
            if c == self.data['word']:
                self.data['busqueda'] = True, {c: v}


    def viewDetails(self):
        print(self.data)
