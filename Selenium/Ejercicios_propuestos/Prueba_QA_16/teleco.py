from selenium.webdriver.common.keys import Keys

from Selenium.Ejercicios_propuestos.Prueba_QA_16.data import data


class teleco(data):

    def __init__(self):
        self.data = data.dataTelefonica

    def OpenWeb(self):
        self.openUrl('Google')

    def searchWeb(self):
        input = self.driver.find_element_by_name(self.data['iGoogle'])
        input.send_keys(self.data['Telefonica'] + Keys.ENTER)
        self.driver.implicitly_wait(10)

    def selectFirsOption(self):
        first = self.driver.find_elements_by_xpath(self.data['fistOption'])[0]
        first.find_element_by_xpath(self.data['link']).click()
        self.driver.implicitly_wait(10)

    def aCookie(self):
        self.acceptCookie()
        self.driver.implicitly_wait(10)

    def getTag(self):
        for val in self.driver.find_elements_by_xpath(self.data['link']):
            self.data['tag'] = [val.get_attribute('href')]
        self.driver.implicitly_wait(20)

    def Accionistas(self):
        self.driver.find_element_by_link_text(self.data['Accionistas']).click()
        self.driver.implicitly_wait(10)

    def switchFrame(self):
        iframe = self.driver.find_element_by_id(self.data['iframe'])
        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text(self.data['Nyse']).click()
        self.driver.implicitly_wait(10)

        for val in self.driver.find_elements_by_css_selector(self.data['valNy']):
            print(val.text)

    def exit(self):
        self.tearDown()
