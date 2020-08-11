import requests


class ApiGet:
    response = ''

    def __init__(self, data):
        self.data = data

    def obtData(self):
        self.response = requests.get(self.data['url'])
        if self.response.status_code == 200:
            self.response = self.response.json()

    def search(self):
        for c, v in self.response.items():
            if c == self.data['sospechoso']:
                print(c, v)
