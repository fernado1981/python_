from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class respuesta4:
    driver = webdriver.Chrome()
    lista = []

    def __init__(self, Accionistas_link_text, First_Option, Url_Google, key_word_Google, Url_Telefonica, Iframe, NY,
                 Get_Data):
        self.Accionistaslinktext = Accionistas_link_text
        self.FirstOption = First_Option
        self.UrlGoogle = Url_Google
        self.KeyWordGoogle = key_word_Google
        self.UrlTelefonica = Url_Telefonica
        self.Iframe = Iframe
        self.NY = NY
        self.GetData = Get_Data

    def openLink(self):
        # abrimos google y buscamos la url de telefónica
        self.driver.get(self.UrlGoogle)
        input = self.driver.find_element_by_name(self.KeyWordGoogle)
        input.send_keys(self.UrlTelefonica)
        input.send_keys(Keys.ENTER)

    def optionfirst(self):
        # selecionamos la primera opcion
        first = self.driver.find_elements_by_xpath(self.FirstOption)[0]
        first.find_element_by_xpath('.//a').click()

    def obtainHref(self):
        # recogemos los Tag pertenecientes a la url
        for val in self.driver.find_elements_by_xpath('//a'):
            self.lista.append(val.get_attribute('href'))

        self.driver.implicitly_wait(10)

    def Accionist(self):
        # click en Accionistas e inversores
        self.driver.find_element_by_link_text(self.Accionistaslinktext).click()

    def obtainvalueNy(self):
        # obtener los valores de la bolsa de ny
        self.driver.maximize_window()
        frame = self.driver.find_element_by_id(self.Iframe)
        self.driver.switch_to.frame(frame)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text(self.NY).click()

        for val in self.driver.find_elements_by_css_selector(self.GetData):
            print(val.text)
            self.lista.append(val.text)

    def showList(self):
        for i in range(len(self.lista)):
            print(self.lista[i])

    def tearDown(self):
        # cierre del driver
        self.driver.quit()
