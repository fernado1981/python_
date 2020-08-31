from POO.ApiTelco.dataTelco import dataTelco


class ApiTelco(dataTelco):

    def __init__(self):
        super().__init__()
        self.data = dataTelco

    def setNews(self, value='Marca'):
        self.data.telco['default'] = value

    def obtnUrl(self):
        for c, v in self.data.telco.items():
            if c == self.data.telco['default']:
                for c, value in v.items():
                    self.data.telco['url'] = value
            break

    def opUrl(self):
        self.data.openURL(self)

    def exit(self):
        self.data.exitBrowser(self)
