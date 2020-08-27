from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Selenium.Ejercicios_propuestos.Prueba_QA_20.data import data


class teleco(data):
    driver = webdriver.Chrome()

    def __init__(self):
        self.data = data.dataTeleco

    def opneBrowser(self):
        self.driver.get(self.data['Google'])
        input = self.driver.find_element_by_name(self.data['Igoogle'])
        input.send_keys(self.data['telefonica'] + Keys.ENTER)
        self.driver.implicitly_wait(10)

    def firstOption(self):
        first = self.driver.find_elements_by_xpath(self.data['first'])[0]
        first.find_element_by_xpath(self.data['link']).click()
        self.driver.implicitly_wait(10)

    def coockies(self):
        self.driver.find_element_by_css_selector(self.data['cookie']).click()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def takeTag(self):
        self.data['dataTag'] = []
        for val in self.driver.find_elements_by_xpath(self.data['link']):
            self.data['dataTag'].append(val.get_attribute('href'))
        self.driver.implicitly_wait(20)

    def Accionistas(self):
        self.driver.find_element_by_link_text(self.data['Acciones']).click()
        self.driver.implicitly_wait(10)

    def valueNY(self):
        iframe = self.driver.find_element_by_id(self.data['iframe'])
        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_link_text(self.data['Nyse']).click()

        for val in self.driver.find_elements_by_css_selector(self.data['valNy']):
            print("entro: ",val.text)

    def exit(self):
        self.driver.quit()
