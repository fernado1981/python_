from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Selenium.Ejercicios_propuestos.Prueba_QA_19.data.DataTeleco import DataTeleco


class telecoQA(DataTeleco):

    driver = webdriver.Chrome()

    def __init__(self):
        self.data = DataTeleco.data

    def openUrl(self):
        self.driver.get(self.data['Google'])
        input = self.driver.find_element_by_name(self.data['IGoogle'])
        input.send_keys(self.data['urlTelefonica'] + Keys.ENTER)
        self.driver.implicitly_wait(10)

    def first(self):
        first = self.driver.find_elements_by_xpath(self.data['firstOption'])[0]
        first.find_element_by_xpath(self.data['link']).click()
        self.driver.implicitly_wait(10)

    def cookie(self):
        self.driver.find_element_by_css_selector(self.data['cookie']).click()
        self.driver.maximize_window()

    def taketag(self):
        count = 0
        for val in self.driver.find_elements_by_xpath('//a'):
            self.data[count] = val.get_attribute(self.data['tagHref'])
            count += 1
        self.driver.implicitly_wait(20)

    def acciones(self):
        self.driver.find_element_by_link_text(self.data['Acciones']).click()
        self.driver.implicitly_wait(10)

    def changeFrame(self):
        iframe = self.driver.find_element_by_id(self.data['iframeID'])
        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('NYSE').click()
        self.driver.implicitly_wait(5)
        for val in self.driver.find_elements_by_css_selector(self.data['valNY']):
            print("tengo",val.text)

    def exit(self):
        self.driver.quit()
