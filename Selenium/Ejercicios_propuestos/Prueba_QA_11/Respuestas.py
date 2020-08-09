import requests


class Respuestas:

    response=''
    def __init__(self, url, sospecha):
        self.sospecha = sospecha
        self.url = url

    def getApi(self):
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            self.response = self.response.json()

    def search(self):
        for c,v in self.response.items():
            if c == self.sospecha:
                print(c,v)

