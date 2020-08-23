from Selenium.Ejercicios_propuestos.Prueba_QA_19.data.DataNews import data


class News(data):

    def __init__(self):
        self.data = data.news
        self.driver=data.driver

    def setNew(self, value='Marca'):
        self.data['prensaDefault'] = value

    def obtUrl(self):
        for c, v in self.data.items():
            if c == self.data['prensaDefault']:
                for c, v in v.items():
                    self.data['url'] = v

    def takeUrl(self):
        url = self.data['url']
        self.driver.get(url)

    def exitDrive(self):
        self.driver.quit()
