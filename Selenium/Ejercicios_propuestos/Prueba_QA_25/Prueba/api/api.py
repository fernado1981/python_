import requests

from Prueba.dts.api_telefonica.api_telefonica import api_telefonica


class api(api_telefonica):

    def __init__(self):
        self.url = self.dt_api_tel['url']
        self.search = self.dt_api_tel['search_word']

    def get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            response = response.json()
            for c, v in response.items():
                if c == self.search:
                    self.dt_api_tel['encontrado'] = True
                    self.dt_api_tel['datos_encontrados'] = v

    def imprime_datos(self):
        print(self.dt_api_tel)
