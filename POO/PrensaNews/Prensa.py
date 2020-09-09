from selenium import webdriver


class Prensa:
    driver = webdriver.Chrome()

    def __init__(self, data):
        self.data = data

    def setNews(self, val='Marca'):
        self.data['default'] = val
        print(self.data['default'])

    def searchUrl(self):
        for c, v in self.data.items():
            if c == self.data['default']:
                for c, v in v.items():
                    self.data['url'] = v
                break

    def openBrowser(self):
        self.driver.get(self.data['url'])

    def closeBrowser(self):
        self.driver.quit()
