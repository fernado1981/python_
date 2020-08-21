from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class dataWeb:
    driver = webdriver.Chrome()

    dataNews = {
        'Marca': {'url': 'http://www.marca.es'},
        'ElMundo': {'url': 'http://www.elmundo.es'},
        'Prensa': 'Marca',
    }

    dataTele = {
        # get
        'Google': 'http://www.google.es',
        # byName
        'iGoogle': 'q',
        # send_Key
        'urlTel': 'https://www.telefonica.com/es',
        # xpath
        'firstOption': "//div[@id='search']//div[@class='g']",
        'link': './/a',
        # cssSelector
        'cookie': '.cc-cookies .cc-cookie-accept',
        'valueNY': '.Tab_Active .last',
        #byId
        'iframe': 'euroland-ticker-es',
        # linkText
        'Accionista': 'Accionistas e inversores',
        'NYSE': 'NYSE',
    }

    def openUrl(self, value=dataTele['Google']):
        self.driver.get(value)
        self.driver.implicitly_wait(10)

    def inputName(self):
        input = self.driver.find_element_by_name(self.dataTele['iGoogle'])
        input.send_keys(self.dataTele['urlTel'] + Keys.ENTER)
        self.driver.implicitly_wait(10)

    def firstOption(self):
        first = self.driver.find_elements_by_xpath(self.dataTele['firstOption'])[0]
        first.find_element_by_xpath(self.dataTele['link']).click()
        self.driver.implicitly_wait(10)

    def cookie(self):
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector(self.dataTele['cookie']).click()
        self.driver.implicitly_wait(10)

    def takeTag(self):
        count = 0
        for val in self.driver.find_elements_by_xpath(self.dataTele['link']):
            self.dataTele[count] = val.get_attribute('href')
            count += 1
        self.driver.implicitly_wait(20)

    def exit(self):
        self.driver.quit()
