from Selenium.Ejercicios_propuestos.POM.hook.SeleniumTest import SeleniumTest


class TelefonicaHome(SeleniumTest):

    def __init__(self):
        super().__init__()
        self.driver = SeleniumTest.driver
        self.data = SeleniumTest.data

    def Cookie(self):
        cookie = self.driver.find_element_by_css_selector(self.data['cookie'])
        cookie.click()
        self.driver.implicitly_wait(5)

    def TakeTag(self, ):
        count = 0
        for val in self.driver.find_elements_by_xpath('//a'):
            self.data[count] = val.get_attribute('href')
            count += 1
        self.driver.implicitly_wait(25)

    def Acciones(self):
        accion = self.driver.find_element_by_link_text(self.data['accion'])
        accion.click()
        self.driver.implicitly_wait(5)
