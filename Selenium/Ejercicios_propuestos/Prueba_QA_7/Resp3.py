from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Resp3:
    driver = webdriver.Chrome()
    lista = []

    def __init__(self, urlGoogle, inputNameGoogle, firstXpathOption, link, urlTelefonica):
        self.urlGoogle = urlGoogle
        self.inputNameGoogle = inputNameGoogle
        self.firstXpathOption = firstXpathOption
        self.link = link
        self.urlTelefonica = urlTelefonica

    def openFirstoption(self):
        self.driver.get(self.urlGoogle)
        input = self.driver.find_element_by_name(self.inputNameGoogle)
        input.send_keys(self.urlTelefonica)
        input.send_keys(Keys.ENTER)

        first = self.driver.find_elements_by_xpath(self.firstXpathOption)[0]
        first.find_element_by_xpath(self.link).click()

    def obtDataRTag(self):
        for val in self.driver.find_elements_by_xpath(self.link):
            if val.get_attribute('href') is None:
                pass
            else:
                self.lista.append(val.get_attribute('href'))

    def showData(self):
        print(self.lista)

    def tearDown(self):
        self.driver.quit()
