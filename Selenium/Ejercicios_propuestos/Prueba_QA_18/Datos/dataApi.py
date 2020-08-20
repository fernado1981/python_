import requests


class data:
    response = ''
    dataApi = {
        'url': 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01',
        'word': 'suspicious_car'
    }

    def getData(self):
        self.response = requests.get(data.dataApi['url'])
        if self.response.status_code == 200:
            self.response = self.response.json()
            return self.response
        else:
            return False

    def searchdata(self, value):
        for c, v in value.items():
            if c == self.dataApi['word']:
                self.dataApi[True] = v
