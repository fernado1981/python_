from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Selenium.Ejercicios_propuestos.Prueba_QA_23.Data import Data


class DataGeneric(Data):
    driver = webdriver.Chrome()
    google = 'http://www.google.es'
    input_google = 'q'

    def openBrowser(self, search=Data.data['telefonica']):
        self.driver.get(self.google)
        input = self.driver.find_element_by_name(self.input_google)
        input.send_keys(search + Keys.ENTER)
        self.driver.implicitly_wait(5)

    def selectOption(self, option_value=0):
        option = self.driver.find_elements_by_xpath("//div[@id='search']//div[@class='g']")[option_value]
        option.find_element_by_xpath('.//a').click()
        self.driver.implicitly_wait(5)

    def closeBrowser(self):
        self.driver.quit()

    def telefonicaHomeCookie(self, cookie=Data.data['cookie']):
        cookies = self.driver.find_element_by_css_selector(cookie)
        cookies.click()
        self.driver.implicitly_wait(5)

    def TakeTag(self, tag=Data.data['tag']):
        count = 0
        for val in self.driver.find_elements_by_xpath(Data.data['link']):
            Data.data[count] = val.get_attribute(tag)
        self.driver.implicitly_wait(25)

    def Acciones(self, Accion=Data.data['Acciones']):
        action = self.driver.find_element_by_link_text(Accion)
        action.click()
        self.driver.implicitly_wait(5)

    def switchFrame(self, iframe=Data.data['iframe']):
        self.driver.maximize_window()
        fm = self.driver.find_element_by_id(iframe)
        self.driver.switch_to.frame(fm)

    def nyse(self, Nyse=Data.data['Nyse']):
        NYSE = self.driver.find_element_by_xpath(Nyse)
        NYSE.click()
        self.driver.implicitly_wait(5)

    def obtValeNY(self, ValNy=Data.data['valNy']):
        for val in self.driver.find_elements_by_css_selector(ValNy):
            print(val.text)

        self.driver.implicitly_wait(10)
