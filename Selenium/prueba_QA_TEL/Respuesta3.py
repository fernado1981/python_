from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Respuesta3:
    driver = webdriver.Chrome()
    lista = []

    def __init__(self, urlGoogle, urlTelefonica, inputGoogle, candidate_first_click, link):
        self.urlGoogle = urlGoogle
        self.urlTelefonicas = urlTelefonica
        self.inpoutGoogle = inputGoogle
        self.candidate_first_click = candidate_first_click
        self.link = link

    def openGoogle(self):
        self.driver.get(self.urlGoogle)
        input = self.driver.find_element_by_css_selector(self.inpoutGoogle)
        input.send_keys(self.urlTelefonicas)
        input.send_keys(Keys.ENTER)

    def firstCandidate(self):
        first = self.driver.find_elements_by_xpath(self.candidate_first_click)[0]
        first.find_element_by_xpath(self.link).click()

    def obtTagHref(self):
        for val in self.driver.find_elements_by_xpath(self.link):
            if val.get_attribute('href') is None:
                pass
            else:
                self.lista.append(val.get_attribute('href'))
                self.driver.implicitly_wait(10)
