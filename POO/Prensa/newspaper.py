from POO.Prensa.data import data


class newspaper(data):

    def __init__(self):
        self.data = data.dataPrensa

    def setNews(self, value='Marca'):
        self.data['default'] = value

    def obtnUrl(self):
        for c, v in self.data.items():
            if c == self.data['default']:
                for c, v in v.items():
                    self.data['url'] = v
                break

    def openurl(self):
        data.openDriver()
