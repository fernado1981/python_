from Selenium.Ejercicios_propuestos.Prueba_QA_16.data import data


class newsPaper(data):

    def __init__(self):
        self.data = data.dataNewspaper

    def setNews(self, news='Marca'):
        self.data['periodico'] = news

    def openNews(self):
        if data.dataNewspaper['periodico'] == 'Marca':
            self.openUrl('Marca')
        else:
            self.openUrl('ElMundo')

    def exit(self):
        self.tearDown()
