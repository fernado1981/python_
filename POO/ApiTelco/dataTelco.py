from selenium import webdriver


class dataTelco:
    telco = {
        'Marca': {'url': 'http://www.marca.es'},
        'ElMundo': {'url': 'http://www.elmundo.es'},
        'default': 'Marca'
    }

    def __init__(self):
        self.driver = webdriver.Chrome()

    def openURL(self):
        url = dataTelco.telco['url']
        print(url)
        self.driver.get(url)

    def exitBrowser(self):
        self.driver.quit()
