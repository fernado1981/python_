from selenium.webdriver.common.keys import Keys

from Selenium.Ejercicios_propuestos.Prueba_QA_21.DataSelenium import DataSelenium


class Teleco(DataSelenium):

    def __init__(self):
        self.driver = DataSelenium.data['driver']
        self.data = DataSelenium.data

    def OpenUrl(self):
        self.driver.get(self.data['google'])

    def searchTelefonica(self):
        input = self.driver.find_element_by_name(self.data['iGoogle'])
        input.send_keys(self.data['iTelco'] + Keys.ENTER)
        self.driver.implicitly_wait(10)

    def firstOption(self):
        first = self.driver.find_elements_by_xpath(self.data['first'])[0]
        first.find_element_by_xpath(self.data['link']).click()
        self.driver.implicitly_wait(10)

    def cookies(self):
        cookie = self.driver.find_element_by_css_selector(self.data['cookie'])
        cookie.click()
        self.driver.implicitly_wait(10)

    def takeTags(self):
        count = 0
        for val in self.driver.find_elements_by_xpath('//a'):
            self.data[count] = val.get_attribute('href')
            count += 1
        self.driver.implicitly_wait(20)

    def Acciones(self):
        acciones = self.driver.find_element_by_link_text(self.data['Acciones'])
        acciones.click()
        self.driver.implicitly_wait(10)

    def valNY(self):
        # busco y entro en el frame
        iframe = self.driver.find_element_by_id(self.data['iframe'])
        self.driver.switch_to.frame(iframe)
        # hago click por xpath en NYSE
        Nyse = self.driver.find_element_by_xpath(self.data['NYSE'])
        Nyse.click()
        self.driver.implicitly_wait(5)
        # obtengo los valores actuales de NY
        for val in self.driver.find_elements_by_css_selector(self.data['valNY']):
            print(val.text)
