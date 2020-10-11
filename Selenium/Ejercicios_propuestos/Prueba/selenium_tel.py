from Prueba.Datos import Datos


class selenium_tel(Datos):

    def __init__(self):
        self.driver = self.datos_Driver['drive']

    def open_web(self):
        self.driver.get(self.datos_web['telefonica'])
        self.driver.implicitly_wait(5)

    def cookie(self):
        self.driver.find_element_by_css_selector(self.datos_web['cookie']).click()
        self.driver.implicitly_wait(5)

    def accionistas(self):
        self.driver.find_element_by_xpath(self.datos_web['accionista']).click()
        self.driver.implicitly_wait(5)

    def change_frame(self):
        self.driver.maximize_window()
        frame = self.driver.find_element_by_id(self.datos_web['frame'])
        self.driver.switch_to.frame(frame)

    def NYse(self):
        self.driver.find_element_by_xpath(self.datos_web['NYSE']).click()

    def valNY(self):
        for val in self.driver.find_elements_by_css_selector(self.datos_web['valNy']):
            print(val.text)

        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()
