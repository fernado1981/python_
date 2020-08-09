from selenium import webdriver


class playUrl:
    url = ''
    prensa = ''

    driver=webdriver.Chrome()

    def __init__(self, data):
        self.datos = data
        self.prensa = "Marca"

    def setPrensa(self, news):
        self.prensa = news

    def obtnUrl(self):
        for c, v in self.datos.items():
            if c == self.prensa:
                print(c, v)
                self.url=v

    def OpenUrl(self):
        self.driver.get(self.url)

    def TearDown(self):
        self.driver.quit()

