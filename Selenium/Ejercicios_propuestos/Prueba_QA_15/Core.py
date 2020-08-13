import requests
from selenium.webdriver.common.keys import Keys

from Data import Data


class Core(Data):
    response = ''

    def __init__(self):
        self.news = Data.DataNews
        self.apiData = Data.dataApi
        self.dataExercise = Data.dataExercise
        self.driver = Data.driver

    def __enter__(self, url):
        self.openurl(url)

    def __exit__(self):
        self.tearDown()

    def setNews(self, new='Marca'):
        self.news['defaultNews'] = new

    def getUrl(self):
        for c, v in self.news.items():
            if c == self.news['defaultNews']:
                for c, v in v.items():
                    self.news['url'] = v
                    return self.news['url']
                break

    def OpenUrl(self):
        self.driver.get(self.news['url'])

    def getData(self):
        self.response = requests.get(self.apiData['url'])
        if self.response.status_code == 200:
            self.response = self.response.json()

    def search(self):
        for c, v in self.response.items():
            if c == self.apiData['search']:
                self.apiData['claveSeachr'] = c
                self.apiData['valueSearch'] = v

    def showData(self):
        for c, v in self.apiData.items():
            print(c, v)

    def searchGoogle(self):
        input = self.driver.find_element_by_name(self.dataExercise['inputNateGoogle'])
        input.send_keys(self.dataExercise['urlSendTelefonica'])
        input.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

    def firstOption(self):
        first = self.driver.find_elements_by_xpath(self.dataExercise['XpathFirstOption'])[0]
        first.find_element_by_xpath(self.dataExercise['linkA']).click()
        self.driver.implicitly_wait(10)

    def Banner(self):
        self.driver.find_element_by_css_selector(self.dataExercise['CssSelectorBanner']).click()
        self.driver.implicitly_wait(10)

    def takeTag(self):
        count = 0
        for val in self.driver.find_elements_by_xpath(self.dataExercise['linkA']):
            self.dataExercise['tag', count + 1] = [val.get_attribute('href')]

        for c, v in self.dataExercise.items():
            print(c, v)

        self.driver.implicitly_wait(10)

    def Accionistas(self):
        self.driver.find_element_by_link_text(self.dataExercise['linkTextAccionistas']).click()
        self.driver.implicitly_wait(10)
        print(self.driver.title)

    def valNY(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        iframe = self.driver.find_element_by_id(self.dataExercise['idIframe'])
        self.driver.switch_to.frame(iframe)

        self.driver.find_element_by_link_text(self.dataExercise['linkTextNyse']).click()
        self.driver.implicitly_wait(10)
        for val in self.driver.find_elements_by_css_selector(self.dataExercise['cssSelectorvalueNy']):
            print(val.text)
