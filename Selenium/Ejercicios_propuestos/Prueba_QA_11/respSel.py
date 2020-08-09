from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class respSel:
    driver = webdriver.Chrome()
    lista = []

    def __init__(self, data):
        self.datos = data

    def openGoogle(self):
        self.driver.get(self.datos['urlGooggle'])
        input = self.driver.find_element_by_name(self.datos['inputGoogleName'])
        input.send_keys(self.datos['urltelefonica'])
        input.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

    def firstoption(self):
        first = self.driver.find_elements_by_xpath(self.datos['firstOptionXpath'])[0]
        first.find_element_by_xpath('.//a').click()
        self.driver.implicitly_wait(10)

    def takeAllTag(self):
        for val in self.driver.find_elements_by_xpath('.//a'):
            self.lista = val.get_attribute('href')
        self.driver.implicitly_wait(20)

    def accpetBanner(self):
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector(self.datos['accepBannerCssSelector']).click()
        self.driver.implicitly_wait(10)

    def Accionistas(self):
        self.driver.find_element_by_link_text(self.datos['AccionistasLinkText']).click()
        self.driver.implicitly_wait(10)

    def valueNY(self):
        iframe = self.driver.find_element_by_id(self.datos['iframeId'])
        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text(self.datos['NyseLinkText']).click()
        self.driver.implicitly_wait(10)
        for val in self.driver.find_elements_by_css_selector(self.datos['valueNY']):
            print(val.text)

    def TearDown(self):
        self.driver.quit()
