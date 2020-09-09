from Selenium.Ejercicios_propuestos.POM.hook.SeleniumTest import SeleniumTest


class TelefonicaAcciones(SeleniumTest):

    def __init__(self):
        super().__init__()
        self.driver = SeleniumTest.driver
        self.data = SeleniumTest.data

    def Euroland(self):
        self.driver.maximize_window()
        iframe = self.driver.find_element_by_id(self.data['euroland'])
        self.driver.switch_to.frame(iframe)

    def NySe(self):
        NYSE = self.driver.find_element_by_xpath(self.data['Nyse'])
        NYSE.click()

    def valNY(self):
        for val in self.driver.find_elements_by_css_selector(self.data['valNY']):
            print(val.text)

        self.driver.implicitly_wait(10)
