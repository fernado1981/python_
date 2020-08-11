import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Respuestas:
    url = ''
    response = ''
    lista = []
    driver = webdriver.Chrome()

    def __init__(self, data):
        self.data = data
        self.marca = data.dataNews['periodico']

    def getdata(self):
        self.response = requests.get(self.data.dataApi['url'])
        if self.response.status_code == 200:
            self.response = self.response.json()

    def busca(self):
        for c, v in self.response.items():
            if c == self.data.dataApi['search']:
                self.lista.append(c)
                self.lista.append(v)

    def showData(self):
        for i in self.lista:
            print(i)

    def setNew(self, news='Marca'):
        self.data.dataNews['periodico'] = news

    def getUrl(self):
        for c, v in self.data.dataNews.items():
            if c == self.data.dataNews['periodico']:
                for c, v in v.items():
                    self.url = v

    def openUrl(self):
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def openGoogle(self):
        self.driver.get(self.data.dataEjercicio['GetGoogle'])
        input = self.driver.find_element_by_name(self.data.dataEjercicio['inputNameGoogle'])
        input.send_keys(self.data.dataEjercicio['sendTelefonica'])
        input.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

    def firstOption(self):
        first = self.driver.find_elements_by_xpath(self.data.dataEjercicio['xpathFirstOption'])[0]
        first.find_element_by_xpath('.//a').click()
        self.driver.implicitly_wait(30)

    def AccepBaner(self):
        self.driver.find_element_by_css_selector(self.data.dataEjercicio['cssSelectorBanner']).click()
        self.driver.implicitly_wait(10)

    def takeTag(self):
        for val in self.driver.find_elements_by_xpath('.//a'):
            self.lista.append(val.get_attribute('href'))
        self.driver.implicitly_wait(30)

    def Accionistas(self):
        self.driver.find_element_by_link_text(self.data.dataEjercicio['linTextAccionistas']).click()
        self.driver.implicitly_wait(10)

    def valueNY(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        iframe = self.driver.find_element_by_id(self.data.dataEjercicio['IdIframe'])
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_link_text(self.data.dataEjercicio['linkTextNYSE']).click()
        self.driver.implicitly_wait(10)

        for val in self.driver.find_elements_by_css_selector(self.data.dataEjercicio['cssSelectorvalueNY']):
            print(val.text)
