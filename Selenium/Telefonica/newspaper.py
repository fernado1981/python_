from selenium import webdriver


class newspaper:
    driver = webdriver.Chrome()
    opnenews=''

    def __init__(self, periodico):
        self.periodicos = periodico
        self.opennews = 'Marca'

    def setnews(self, news):
        self.opennews = news

    def obtenerUrl(self):
        for c, v in self.periodicos.items():
            if c == self.opennews:
                for c, v in v.items():
                    self.driver.get(v)
                    print(self.driver.title)

    def tearDown(self):
        self.driver.quit()
