import requests
from selenium import webdriver


class Respuestas:
    response = ''
    lista = []
    driver = webdriver.Chrome()

    def __init__(self, data):
        self.dataApi = data.dataApi
        self.dataNew = data.dataNews

    def getData(self):
        self.response = requests.get(self.dataApi['url'])
        if self.response.status_code == 200:
            self.response = self.response.json()

    def searchData(self):
        for c, v in self.response.items():
            if c == self.dataApi['search']:
                self.lista.append(c)
                self.lista.append(v)
            elif c == self.dataApi['search1']:
                for c, v in v.items():
                    for c, v in v.items():
                        self.lista.append(c)
                        self.lista.append(v)
            else:
                pass

    def showData(self):
        for i in self.lista:
            print(i)

    def setNews(self, News='Marca'):
        self.dataNew['periodico'] = News

    def ObtnUrl(self):
        for c, v in self.dataNew.items():
            if c == self.dataNew['periodico']:
                for c, v in v.items():
                    self.dataNew['url'] = v
                    print(self.dataNew['url'])
                break

    def openUrl(self):
        self.driver.get(self.dataNew['url'])
