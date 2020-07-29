import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ejercicio_prueba:
    api = ''
    lista = {}
    listaTelefonica = []
    sospechosos = []

    def __init__(self, dic):
        self.diccionario = dic
        self.periodico = 'Marca'
        self.url_Google = 'https://www.google.es'

    def setPeriodico(self, news):
        self.periodico = news

    def ShowDiccionario(self):
        for c, v in self.diccionario.items():
            if c == self.periodico:
                for c, v in v.items():
                    return v

    def setUrl(self, url):
        self.url_Google = url

    def openUrl(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        print(driver.title)

    def setApi(self, api_url):
        self.url_Google = api_url

    def apiGet(self):
        response = requests.get(self.url_Google)
        print(response.status_code)
        arr = response.json()

        for c, v in arr.items():
            if c == 'suspicious_car':
                self.lista[c] = v
                self.sospechosos.append(self.lista)
        print(self.sospechosos)

    def searchTelefonica(self, url):
        driver = webdriver.Chrome()
        driver.get(self.url_Google)
        word = driver.find_element_by_css_selector("input[name='q']")
        word.send_keys(url, '' + Keys.ENTER)
        # buscamos el primer link candidato de telefónica y hacemos click
        candidate = driver.find_elements_by_xpath("//div[@id='search']//div[@class='g']")[0]
        candidate.find_element_by_xpath('.//a').click()
        driver.implicitly_wait(10)
        print(driver.title)

    def listadosTelefónica(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(10)

        for a in driver.find_elements_by_xpath('.//a'):
            self.listaTelefonica.append(a.get_attribute('href'))

    def accionistas(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(10)
        Accionistas = driver.find_element_by_css_selector("a[title='Ir a Accionistas e inversores '")
        Accionistas.click()
        assert driver.title == 'Accionistas e Inversores | Accionistas e Inversores | Telefónica', "problem"

    def bolsaNYSE(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        Accionistas = driver.find_element_by_css_selector("a[title='Ir a Accionistas e inversores '")
        Accionistas.click()
        iframe = driver.find_element_by_css_selector("#euroland-ticker-es")
        driver.switch_to.frame(iframe)
        driver.implicitly_wait(10)
        driver.find_element_by_link_text('NYSE').click()
        driver.implicitly_wait(10)
        data = driver.find_elements_by_xpath("//div[contains(@class,'Tab_Active')]//span[@class='last']")

        for i in data:
            assert i.text == '4,45', "problem"


