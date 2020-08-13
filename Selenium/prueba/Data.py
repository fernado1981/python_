from selenium import webdriver


class Data:
    driver = webdriver.Chrome()

    DataNews = {
        'Marca': {'url': 'http://www.marca.es'},
        'ElMundo': {'url': 'http://www.elmundo.es'},
        'defaultNews': 'Marca'
    }

    dataApi = {
        'url': 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01',
        'search': 'suspicious_car'
    }

    dataExercise = {
        'getGoogle': 'http://www.google.es',
        'inputNateGoogle': 'q',
        'urlSendTelefonica': 'https://www.telefonicas.com/es',
        'XpathFirstOption': "//div[@id='search']//div[@class='g']",
        'linkA': './/a',
        'CssSelectorBanner': '.cc-cookies .cc-cookie-accept',
        'linkTextAccionistas': 'Accionistas e inversores',
        'idIframe': 'euroland-ticker-es',
        'linkTextNyse': 'NYSE',
        'cssSelectorvalueNy': '.Tab_Active .last'
    }

    def openurl(self, url='none'):
        if url == 'none':
            pass
        elif url == 'Google':
            self.driver.get(Data.dataExercise['getGoogle'])
        else:
            self.driver.get(url)

    def tearDown(self):
        self.driver.quit()
