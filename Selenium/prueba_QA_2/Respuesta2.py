import requests


class Respuesta2:
    lista = []

    def __init__(self, url_api, sospechosos):
        self.url = url_api
        self.search = sospechosos

    def obtValueApi(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            response = response.json()
            for c, v in response.items():
                self.lista.append(c)
                self.lista.append(v)
