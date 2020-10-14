from ejercicio_repaso.datos import datos


class web(datos):

    def __init__(self):
        self.driver = self.drive['driver']
        self.datos = self.dts_web

    def open_url(self):
        self.driver.get(self.datos['telefonica'])
        self.driver.implicitly_wait(5)

    def cookie(self):
        self.driver.find_element_by_css_selector(self.datos['cookie']).click()
        self.driver.implicitly_wait(5)

    def acciones(self):
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(self.datos['acciones']).click()
        self.driver.implicitly_wait(10)

    def euro(self):
        frame = self.driver.find_element_by_id(self.datos['euroland'])
        self.driver.switch_to.frame(frame)
        self.driver.implicitly_wait(5)

    def nyse(self):
        self.driver.find_element_by_xpath(self.datos['NYSE']).click()

    def take_val(self):
        for val in self.driver.find_elements_by_css_selector(self.datos['valny']):
            print(val.text)

        self.driver.implicitly_wait(10)