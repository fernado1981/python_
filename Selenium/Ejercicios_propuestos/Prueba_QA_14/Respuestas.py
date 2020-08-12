import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Respuestas:
    response = ''
    lista = []
    #driver = webdriver.Chrome()

    def __init__(self, data):
        self.driver = data.driver
        self.dataApi = data.dataApi
        self.dataNew = data.dataNews
        self.exercise = data.dataExercise

    def getData(self):
        self.response = requests.get(self.dataApi['url'])
        if self.response.status_code == 200:
            self.response = self.response.json()

    def searchData(self):
        for c, v in self.response.items():
            if c == self.dataApi['search']:
                self.lista.append(c)
                self.lista.append(v)
            elif c == self.dataApi['search1']:
                for c, v in v.items():
                    for c, v in v.items():
                        self.lista.append(c)
                        self.lista.append(v)
            else:
                pass

    def showData(self):
        for i in self.lista:
            print(i)

    def setNews(self, News='Marca'):
        self.dataNew['periodico'] = News

    def ObtnUrl(self):
        for c, v in self.dataNew.items():
            if c == self.dataNew['periodico']:
                for c, v in v.items():
                    self.dataNew['url'] = v
                break

    def openUrl(self):
        self.driver.get(self.dataNew['url'])

    def tearDown(self):
        self.driver.quit()

    def openGoogle(self):
        self.driver.get(self.exercise['getGoogle'])
        input = self.driver.find_element_by_name(self.exercise['iGoogleName'])
        input.send_keys(self.exercise['sendUrlTel'])
        input.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

    def firstoption(self):
        first = self.driver.find_elements_by_xpath(self.exercise['firstOptionXpath'])[0]
        first.find_element_by_xpath(self.exercise['link']).click()
        self.driver.implicitly_wait(10)

    def acceptbanner(self):
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector(self.exercise['BannerCss']).click()
        self.driver.implicitly_wait(10)
    def taketag(self):
        for val in self.driver.find_elements_by_xpath(self.exercise['link']):
            self.lista.append(val.get_attribute('href'))
        self.driver.implicitly_wait(25)

    def Accionista(self):
        self.driver.find_element_by_link_text(self.exercise['AccionistaslinkText']).click()
        self.driver.implicitly_wait(10)

    def valueNY(self):
        iframe=self.driver.find_element_by_id(self.exercise['iframeId'])
        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text(self.exercise['nyseLinkText']).click()
        self.driver.implicitly_wait(10)

        for val in self.driver.find_elements_by_css_selector(self.exercise['valNYCss']):
                    print(val.text)
