from selenium import webdriver


class dataWeb:
    driver = webdriver.Chrome()

    dataNews = {
        'Marca': {'url': 'http://www.marca.es'},
        'ElMundo': {'url': 'http://www.elmundo.es'},
        'Prensa': 'Marca',
    }

    def openUrl(self, value):
        self.driver.get(value)

    def exit(self):
        self.driver.quit()
