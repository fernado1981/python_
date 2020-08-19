from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class data:
    dataNews = {
        'Marca': {'url': 'http://www.marca.es'},
        'ElMundo': {'url': 'http://www.elmundo.es'},
        'periodico': 'Marca'
    }
    dataSelTeleco = {
        # get
        'Google': 'http://www.google.es',
        # byName
        'iGoogle': 'q',
        # send_Key
        'teleco': 'https://www.telefonica.com/es',
        # Xpath
        'firsOption': "//div[@id='search']//div[@class='g']",
        'link': './/a',
        # cssSelector
        'cookie': '.cc-cookies .cc-cookie-accept',
        'valNY': '.Tab_Active .last',
        # linkText
        'Accionistas': 'Accionistas e inversores',
        'NYSE': 'NYSE',
        # Id
        'iframe': 'euroland-ticker-es',
    }
#driver
    driver = webdriver.Chrome()

    def openUrl(self, url):
        if url == 'Google':
            self.driver.get(self.dataSelTeleco['Google'])
            input = self.driver.find_element_by_name(self.dataSelTeleco['iGoogle'])
            input.send_keys(self.dataSelTeleco['teleco'] + Keys.ENTER)
            self.driver.implicitly_wait(10)
        else:
            self.driver.get(url)

    def tearDown(self):
        self.driver.quit()


# selenium
