from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class RespuestaQA:
    driver = webdriver.Chrome()
    equipo = ''
    url = ''
    listaTag=[]
    Google = 'http://www.google.es'
    inputNameGoogle = 'q'
    urlTel = 'https://www.telefonica.com/es'
    firstXpath="//div[@id='search']//div[@class='g']"
    AccionistasLinkText='Accionistas e Inversores'
    popUpDownAccpetId=".cc-cookies #aceptar"
    iframeId='euroland-ticker-es'
    NYSELinkText='NYSE'
    valueNY='.Tab_Active .last'

    def __init__(self, equipos):
        self.equipos = equipos
        self.equipo = 'Madrid'

    def setEquipo(self, equipo):
        self.equipo = equipo

    def obtnUrl(self):
        for c, v in self.equipos.items():
            if self.equipo == c:
                self.url = v
                print(self.url)

    def openUrl(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def openGoogle(self):
        self.driver.get(self.Google)

    def buscar(self):
        input = self.driver.find_element_by_name(self.inputNameGoogle)
        input.send_keys(self.urlTel)
        input.send_keys(Keys.ENTER)

    def takeFirstoption(self):
        firstOption = self.driver.find_elements_by_xpath(self.firstXpath)[0]
        firstOption.find_element_by_xpath('.//a').click()

    def takeAttributetag(self):
        for val in self.driver.find_elements_by_xpath('.//a'):
            self.listaTag.append(val.get_attribute('href'))
            self.driver.implicitly_wait(20)

    def Accionistas(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.driver.find_element_by_link_text(self.AccionistasLinkText).click()
        self.driver.implicitly_wait(10)

    def popUpDown(self):
        popUp = self.driver.find_element_by_css_selector(self.popUpDownAccpetId)
        popUp.click()

    def obtnNYValue(self):
        frame = self.driver.find_element_by_id(self.iframeId)
        self.driver.switch_to.frame(frame)
        self.driver.find_element_by_link_text(self.NYSELinkText).click()
        for val in self.driver.find_elements_by_css_selector(self.valueNY):
            print(val.text)

    def TearDown(self):
        self.driver.quit()








