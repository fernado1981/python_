from Selenium.Ejercicios_propuestos.Prueba_QA_17.Data.data import data


class teleco(data):

    def __init__(self):
        self.data = data
        self.driver = data.driver

    def firstOption(self):
        first = self.driver.find_elements_by_xpath(self.dataSelTeleco['firsOption'])[0]
        first.find_element_by_xpath(self.dataSelTeleco['link']).click()
        self.driver.implicitly_wait(10)

    def cookie(self):
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector(self.dataSelTeleco['cookie']).click()
        self.driver.implicitly_wait(10)

    def tagRef(self):
        for val in self.driver.find_elements_by_xpath(self.dataSelTeleco['link']):
            print(val.get_attribute('href'))
        self.driver.implicitly_wait(20)

    def Acciones(self):
        self.driver.find_element_by_link_text(self.dataSelTeleco['Accionistas']).click()
        self.driver.implicitly_wait(10)

    def valueNY(self):
        iframe = self.driver.find_element_by_id(self.dataSelTeleco['iframe'])
        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text(self.dataSelTeleco['NYSE']).click()

        for val in self.driver.find_elements_by_css_selector(self.dataSelTeleco['valNY']):
            print(val.text)
