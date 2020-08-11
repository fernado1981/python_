from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class exerciseTest:
    driver = webdriver.Chrome()
    lista=[]
    def __init__(self, data):
        self.data = data

    def openNavigator(self):
        self.driver.get(self.data['urlGoogle'])
        input = self.driver.find_element_by_name(self.data['iGooglName'])
        input.send_keys(self.data['urlTel'])
        input.send_keys(Keys.ENTER)

    def firstOption(self):
        self.driver.implicitly_wait(10)
        first = self.driver.find_elements_by_xpath(self.data['firstOptionXpath'])[0]
        first.find_element_by_xpath('.//a').click()
        self.driver.implicitly_wait(10)

    def AcceptBanner(self):
        self.driver.find_element_by_css_selector(self.data['AccpetBanner']).click()
        self.driver.implicitly_wait(10)

    def taketag(self):
        for val in self.driver.find_elements_by_xpath('.//a'):
            lista.appen(val.get_attribute('href'))
        self.driver.implicitly_wait(20)

    def Accionistas(self):
        self.driver.find_element_by_link_text(self.data['Accionistas']).click()
        self.driver.implicitly_wait(10)

    def valueNY(self):
        iframe = self.driver.find_element_by_id(self.data['iframeId'])
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_link_text(self.data['NYSELinkText']).click()
        self.driver.implicitly_wait(10)
        for val in self.driver.find_elements_by_css_selector(self.data['valueNY']):
            print(val.text)

    def tearDown(self):
        self.driver.quit()
