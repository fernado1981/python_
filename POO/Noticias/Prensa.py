from POO.Noticias.DataPrensa import DataPrensa


class Prensa(DataPrensa):

    def __init__(self):
        super().__init__()

    def setNews(self, value='Marca'):
        self.defaultNews = value

    def getUrl(self):
        self.getUrlNews()

    def openBrowser(self):
        self.openUrl()
