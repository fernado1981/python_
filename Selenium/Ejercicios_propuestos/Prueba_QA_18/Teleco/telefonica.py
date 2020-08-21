from selenium.webdriver.common.keys import Keys

from Selenium.Ejercicios_propuestos.Prueba_QA_18.Datos.dataWeb import dataWeb


class telefonica(dataWeb):

    def __init__(self):
        self.data = dataWeb
        self.driver = dataWeb.driver

    def acciones(self):
        self.driver.find_element_by_link_text(self.dataTele['Accionista']).click()
        self.driver.implicitly_wait(10)

    def switchFrame(self):
        iframe = self.driver.find_element_by_id(self.dataTele['iframe'])
        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(10)

    def changeValueNY(self):
        self.driver.find_element_by_link_text(self.dataTele['NYSE']).click()
        self.driver.implicitly_wait(10)

    def getValueNY(self):
        for val in self.driver.find_elements_by_css_selector(self.dataTele['valueNY']):
            print(val.text)



