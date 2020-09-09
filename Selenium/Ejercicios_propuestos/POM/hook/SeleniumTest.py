from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Selenium.Ejercicios_propuestos.POM.Locator.DataLocators import DataLocators


class SeleniumTest(DataLocators):
    driver = webdriver.Firefox()

    def __init__(self):
        self.data = DataLocators.data

    def OpenBrowser(self):
        self.driver.get(self.data['Google'])
        input = self.driver.find_element_by_name(self.data['Igoogle'])
        input.send_keys(self.data['telefonica'] + Keys.ENTER)
        self.driver.implicitly_wait(5)

    def firstOpt(self):
        first = self.driver.find_elements_by_xpath(self.data['FirstOption'])[0]
        first.find_element_by_xpath(self.data['link']).click()
        self.driver.implicitly_wait(5)

    def closeBrowser(self):
        self.driver.quit()
