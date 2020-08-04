from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class respuesta3:
    driver = webdriver.Chrome()
    lista = []

    def __init__(self, urlgetGoogle, byNameGoogle, urlgetTel, firstXpathOption, link):
        self.urlgetGoogle = urlgetGoogle
        self.byNameGoogle = byNameGoogle
        self.urlgetTel = urlgetTel
        self.firstXpathOption = firstXpathOption
        self.link = link

    def openNavigator(self):
        self.driver.get(self.urlgetGoogle)
        input = self.driver.find_element_by_name(self.byNameGoogle)
        input.send_keys(self.urlgetTel)
        input.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

    def searchFirstoption(self):
        first = self.driver.find_elements_by_xpath(self.firstXpathOption)[0]
        first.find_element_by_xpath(self.link).click()
        self.driver.implicitly_wait(10)

    def obtlistTag(self):
        for val in self.driver.find_elements_by_xpath(self.link):
            self.lista.append(val.get_attribute('href'))
        print(self.lista)
        self.driver.implicitly_wait(20)
