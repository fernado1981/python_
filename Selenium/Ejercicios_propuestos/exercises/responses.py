from pip._vendor import requests


class responses:
    response = ''

    def __init__(self, url, sospecha):
        self.url = url
        self.sospecha = sospecha

    def getApi(self):
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            self.response = self.response.json()

    def search(self):
        for c, v in self.response.items():
            if c == self.sospecha:
                print(c, v)
