from selenium import webdriver


class NewsPaperData:
    periodico = ''
    url = ''
    driver=webdriver.Chrome()

    def __init__(self, data):
        self.data = data
        self.periodico = 'Marca'

    def setPeriodico(self, newPer):
        self.periodico = newPer


    def ObtenUrl(self):
        for c, v in self.data.items():
            if c == self.periodico:
                for c,v in v.items():
                    self.url=v

    def showUrl(self):
        print(self.url)

    def openUrl(self):
        self.driver.get(self.url)

    def TearDown(self):
        self.driver.quit()
