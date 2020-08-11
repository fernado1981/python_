from selenium import webdriver

class Prensa:
    driver = webdriver.Chrome()
    marca = ''
    url = ''

    def __init__(self, data):
        self.data = data
        self.marca = 'Marca'

    def setNew(self, param):
        self.marca = param

    def obtnUrl(self):
        for c, v in self.data.items():
            if c == self.marca:
                for c, v in v.items():
                    self.url = v
                    return self.url

    def openUrl(self):
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

