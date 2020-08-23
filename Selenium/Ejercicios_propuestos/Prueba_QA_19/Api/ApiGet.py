import requests

from Selenium.Ejercicios_propuestos.Prueba_QA_19.data.DataApi import data


class ApiGet(data):
    response = ''

    def __init__(self):
        self.data = data.dataApiGet

    def getData(self):
        self.response = requests.get(self.data['url'])
        if self.response.status_code == 200:
            self.response = self.response.json()

    def seacrh(self):
        for c, v in self.response.items():
            if c == self.data['searchWord']:
                self.data[True] = v

    def showData(self):
        print(self.data)
