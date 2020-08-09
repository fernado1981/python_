import requests


class ApiGet:
    def __init__(self, data):
        self.datos = data

    def GetApi(self):
        response = requests.get(self.datos['url'])
        if response.status_code == 200:
            response = response.json()
            for c, v in response.items():
                if c == self.datos['sospechoso']:
                    self.datos[c] = True
                    self.datos['color_Suspicious'] = v

    def showData(self):
        for c, v in self.datos.items():
            print(c, v)

        print(self.datos)
