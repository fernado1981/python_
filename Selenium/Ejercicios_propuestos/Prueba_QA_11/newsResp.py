class newsResp:
    news = ''

    def __init__(self, periodico):
        self.periodico = periodico
        self.news = 'Marca'

    def setNews(self, new):
        self.news = new

    def obtenUrl(self):
        for c, v in self.periodico.items():
            if c == self.news:
                print(c, v)
