import requests

from Prueba.Datos import Datos


class Telefonica(Datos):

    def __init__(self):
        self.Url = Datos.datos_Api['url_get']
        self.search = Datos.datos_Api['search_word']
        self.Url_post = Datos.datos_Api['url_post']
        self.DS = Datos.datos_Api['url_post']

    def get_api(self):
        response = requests.get(self.Url)
        if response.status_code == 200:
            response = response.json()
            for c, v in response.items():
                if c == self.search:
                    self.datos_Api['encontrado'] = True
                    self.datos_Api['suspicius_values'] = v

    def imprimir_datos(self):
        for c, v in self.datos_Api.items():
            print(c, v)

    def post_api(self, val={'nombre': 'foo'}):
        response = requests.post(self.Url_post, val, stream=True)
        if response.status_code == 201:
            response = response.json()
            for c, v in response.items():
                print(c, v)
