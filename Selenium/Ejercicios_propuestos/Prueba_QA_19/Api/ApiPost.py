import requests

from Selenium.Ejercicios_propuestos.Prueba_QA_19.data.DataApi import data


class ApiPost(data):
    response = ''

    def __init__(self):
        self.url = data.dataApiPost['url']
        self.value = data.dataApiPost['value']

    def postData(self):
        self.response = requests.post(self.url, self.value, stream=True)
        if self.response.status_code == 201:
            self.response = self.response.json()
            self.response.pop('id')
            self.dataApiPost['datos'] = self.response

    def showData(self):
        for c, v in self.dataApiPost['value'].items():
            for z, y in self.dataApiPost['datos'].items():
                if v == y:
                    self.dataApiPost['Result'] = True


    def result(self):
        if self.dataApiPost['Result']:
            print("Iguales: ")
            print('value: ', self.dataApiPost['value'])
            print('valueExpected: ', self.dataApiPost['datos'])
