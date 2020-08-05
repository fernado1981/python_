from selenium import webdriver


class Resp4:
    driver = webdriver.Chrome()

    def __init__(self, urlTelefonica, AccionesLink, iframe, NyseLink, valuesByNy):
        self.urlTel = urlTelefonica
        self.AccionesLink = AccionesLink
        self.iframeid = iframe
        self.NyseLink = NyseLink
        self.valuesByNy = valuesByNy

    def openUrl(self):
        # abrimos la url de telefónica
        self.driver.get(self.urlTel)
        self.driver.implicitly_wait(10)

    def Acciones(self):
        # hacemos click en acciones
        self.driver.find_element_by_link_text(self.AccionesLink).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector('.cc-cookies #aceptar').click()

    def valuesNy(self):
        # maximizamos el window
        self.driver.maximize_window()

        # cambiamos al frame
        frames = self.driver.find_element_by_id(self.iframeid)
        self.driver.switch_to.frame(frames)
        self.driver.implicitly_wait(10)

        # click en NYSE
        tap = self.driver.find_element_by_link_text(self.NyseLink)
        tap.click()

        # obtenemos los valores
        for val in self.driver.find_elements_by_css_selector(self.valuesByNy):
            print(val.text)

    def terDown(self):
        self.driver.quit()
