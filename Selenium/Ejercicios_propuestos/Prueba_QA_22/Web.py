from Selenium.Ejercicios_propuestos.Prueba_QA_22.DataWeb import DataWeb


class Web(DataWeb):

    def __init__(self):
        super().__init__()

    def goGoogle(self):
        self.openBrowser()

    def searchInput(self):
        self.search()

    def firstOptionPress(self):
        self.fristOption()

    def acceptCookie(self):
        self.cookie()

    def takeValTag(self):
        self.takeTag()

    def accionesPress(self):
        self.acciones()

    def obtnValNy(self):
        self.vlaNy()

    def quitDriver(self):
        self.quit()