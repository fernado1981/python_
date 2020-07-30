from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class selenium3:
    driver = webdriver.Chrome()
    lista = []

    def __init__(self, url, url_search):
        self.URl = url
        self.urlSearch = url_search

    def openGoogle(self):
        self.driver.get(self.URl)
        input = self.driver.find_element_by_css_selector("input[name='q']")
        input.send_keys(self.urlSearch)
        input.send_keys(Keys.ENTER)

        search = self.driver.find_elements_by_xpath("//div[@id='search']//div[@class='g']")[0]
        search.find_element_by_xpath(".//a").click()

    def obtTags(self):
        for a in self.driver.find_elements_by_xpath(".//a"):
            self.lista.append(a.get_attribute('href'))
        print(len(self.lista))

    def tearDown(self):
        self.driver.quit()
