from selenium import webdriver


class data:
    driver = webdriver.Chrome()

    dataApi = {
        'url': 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01',
        'word': 'suspicious_car'
    }
    dataNewspaper = {
        'Marca': {'url': 'http://www.marca.es'},
        'ElMundo': {'url': 'http://.www.elmundo.es'},
        'periodico': 'Marca'
    }
    dataTelefonica = {
        # get
        'Google': 'http://www.google.es',
        # inputName
        'iGoogle': 'q',
        # send_key
        'Telefonica': 'https://www.telefonica.com/es',
        # xpath
        'fistOption': "//div[@id='search']//div[@class='g']",
        'link': './/a',
        # linkText
        'Accionistas': 'Accionistas e inversores',
        'Nyse': 'NYSE',
        # frame Id
        'iframe': 'euroland-ticker-es',
        # cssSelector
        'valNy': '.Tab_Active .last',
        'cookie': '.cc-cookies .cc-cookie-accept'
    }

    def openUrl(self, item='Google'):
        if item == 'Marca':
            self.driver.get(data.dataNewspaper['Marca']['url'])
        elif item == 'ElMundo':
            self.driver.get(data.dataNewspaper['ElMundo']['url'])
        elif item == 'Google':
            self.driver.get(data.dataTelefonica['Google'])
        else:
            pass

    def tearDown(self):
        self.driver.quit()

    def acceptCookie(self):
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector(data.dataTelefonica['cookie']).click()
