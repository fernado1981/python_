class ObtUrl:
    periodico = ''
    url = ''
    driver = webdriver.bing()

    def __init__(self, prensa):
        self.periodicos = prensa
        self.periodico = 'marca'

    def setPeriodico(self, news):
        self.periodico = news.lower()

    def obtnUrl(self):
        for c, v in self.periodicos.items():
            c = c.lower()
            if c == self.periodico:
                self.url = v

    def OpenUrl(self):
        self.driver.get(self.url)
