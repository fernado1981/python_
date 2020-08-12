from selenium.webdriver.chrome import webdriver


class newspaper:
    url = ''
    news = ''
    driver = webdriver

    def __init__(self, data):
        self.data = data
        self.news = 'Marca'

    def setNews(self, param):
        self.news = param

    def obtnUrl(self):
        for c,v in self.data.items():
            if c == self.news:
                for c, v in v.items():
                    self.url = v

    def openUrl(self):
        self.driver.WebDriver.get(self.url)