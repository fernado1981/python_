import requests


class dataApi:
    dataApiGet = {
        'url': 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01',
        'word': 'suspicious_car'
    }

    # Api
    def getData(self):
        self.response = requests.get(self.dataApiGet['url'])
        if self.response.status_code == 200:
            self.response = self.response.json()
        else:
            print("Error")

    def searchData(self):
        for c, v in self.response.items():
            if c == self.dataApiGet['word']:
                self.dataApiGet[True] = v
