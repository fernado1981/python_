from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class pruebaAmazon:
    driver = webdriver.Chrome()

    def __init__(self, urlGoogle, KeyWordGoogle, SearchAmazon, searchFirstoption, AcceptCookie, inputAmazon):
        self.urlGoogle = urlGoogle
        self.KeyWordGoogle = KeyWordGoogle
        self.SearchAmazon = SearchAmazon
        self.searchFirstoptions = searchFirstoption
        self.AcceptCookie = AcceptCookie
        self.inputAmazon = inputAmazon

    def OpenAmazon(self):
        self.driver.get(self.urlGoogle)
        self.driver.maximize_window()
        input = self.driver.find_element_by_name(self.KeyWordGoogle)
        input.send_keys(self.SearchAmazon)
        input.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        first = self.driver.find_elements_by_xpath(self.searchFirstoptions)[0]
        first.find_element_by_xpath('.//a').click()

    def AcceptTerms(self):
        self.driver.find_elements_by_css_selector(self.AcceptCookie).click()

    def searchChoose(self, buscar):
        input = self.driver.find_element_by_css_selector(self.inputAmazon)
        input.send_keys(buscar)
        input.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

    def selecionarPrenda(self, index):
        indice = self.driver.find_element_by_xpath(index)
        self.driver.execute_script("arguments[0].scrollIntoView();", indice)
        indice.click()
