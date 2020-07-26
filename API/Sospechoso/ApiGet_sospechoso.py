import requests


class apiget_sospechoso:
    response = {}
    listaSospechosos = []

    def __init__(self, url, search):
        self.url = url
        self.search = search

    def getData(self):
        self.response = requests.get(self.url)
        print(self.response.status_code)
        self.response = self.response.json()

    def searchData(self):
        for c, v in self.response.items():
            if c == self.search:
                self.listaSospechosos.append(c)
                self.listaSospechosos.append(v)

    def viewlist(self):
        print(self.listaSospechosos)
