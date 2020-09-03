import requests

from API.Buscar.DataBusca import DataBusca


class Busca(DataBusca):
    response = ''

    def __init__(self):
        self.buscar = DataBusca.data['search']
        self.url = DataBusca.data['url']
        self.DataBusca = DataBusca.data

    def apiGet(self):
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            self.response = self.response.json()
        else:
            print("Error")

    def searchWord(self):
        for c, v in self.response.items():
            if c == self.buscar:
                self.DataBusca['Encontrado'] = True, {c: v}

    def verDatos(self):
        for c, v in self.DataBusca.items():
            print(c, v)
