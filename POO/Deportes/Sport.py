from POO.Deportes.DataSport import DataSport
from POO.Generic.hook import hook


class Sport(hook):

    def __init__(self):
        self.data = DataSport.data

    def setSport(self, value='Marca'):
        self.data['DefaultSport'] = value.lower()

    def obtnUrl(self):
        for c, v in self.data.items():
            if c.lower() == self.data['DefaultSport']:
                print(True)
                for c, v in v.items():
                    print(v)
                    self.data['urlDefault'] = v
                break

    def openDriver(self):
        self.openBrowser(self.data['urlDefault'])

    def closeDriver(self):
        self.quitDriver()
