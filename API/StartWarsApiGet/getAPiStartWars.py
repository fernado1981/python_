import requests

from API.getApi.data import data


class getApiStartWars(data):
    response = ''

    def __init__(self):
        self.urlBase = data.dataApiGetSW['url']

    def getData(self):

        self.response = requests.get(self.urlBase)
        if self.response.status_code == 200:
            self.response = self.response.json()

    def showData(self, value='people'):
        if value == 'vehicles' or value == 'starships':
            print(value.upper())
            for c, v in self.response.items():
                if value == c:
                    self.response = requests.get(v)
                    if self.response.status_code == 200:
                        self.response = self.response.json()
                        for c, v in self.response.items():
                            if c == 'results':
                                for i in range(len(v)):
                                    print('Nombre: ', v[i]['name'], ' Modelo: ', v[i]['model'], ' url: ', v[i]['url'])
        elif value == 'species':
            print(value.upper())
            for c, v in self.response.items():
                if c == value:
                    self.response = requests.get(v)
                    if self.response.status_code == 200:
                        self.response = self.response.json()
                        for c, v in self.response.items():
                            if c == 'results':
                                for i in range(len(v)):
                                    print('Nombre: ', v[i]['name'], ' Clasificacion: ', v[i]['classification'],
                                          ' Url: ', v[i]['url'])

        elif value == 'planets':
            print(value.upper())
            for c, v in self.response.items():
                if c == value:
                    self.response = requests.get(v)
                    if self.response.status_code == 200:
                        self.response = self.response.json()
                        for c, v in self.response.items():
                            if c == 'results':
                                for i in range(len(v)):
                                    print('Nombre: ', v[i]['name'], ', diametro: ', v[i]['diameter'], ', Terreno: ',
                                          v[i]['terrain'], ', residentes: ', v[i]['residents'])

        elif value == 'people':
            print(value.upper())
            for c, v in self.response.items():
                if c == value:
                    self.response = requests.get(v)
                    if self.response.status_code == 200:
                        self.response = self.response.json()
                        for c, v in self.response.items():
                            if c == 'results':
                                for i in range(len(v)):
                                    print('Nombre: ', v[i]['name'], ',Genero: ', v[i]['gender'], ', Pais: ',
                                          v[i]['homeworld'], ',Peliculas: ', v[i]['films'], ', url: ', v[i]['url'])
