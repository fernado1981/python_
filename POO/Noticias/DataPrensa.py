from selenium import webdriver


class DataPrensa:
    data = {
        'Marca': {'url': 'http://www.marca.es'},
        'ElMundo': {'url': 'http://www.elmundo.es'},
        'defaulNews': 'Marca',
        'driver': webdriver.Chrome()
    }

    def __init__(self):
        self.driver = self.data['driver']
        self.data = self.data
        self.defaultNews = self.data['defaulNews']

    def getUrlNews(self):
        for c, v in self.data.items():
            if c == self.defaultNews:
                for c, v in v.items():
                    self.data['url'] = v
                break
            else:
                print("Error")

    def openUrl(self):
        self.driver.get(self.data['url'])

