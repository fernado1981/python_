from selenium import webdriver


class Respuesta4:
    driver = webdriver.Chrome()

    def __init__(self, urlTel, Accionista):
        self.urlTelefonica = urlTel
        self.Accionistas = Accionista

    def openAccionista(self):
        self.driver.get(self.urlTelefonica)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text(self.Accionistas).click()

        print(self.driver.title)
