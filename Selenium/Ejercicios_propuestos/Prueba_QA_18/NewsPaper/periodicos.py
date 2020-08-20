from Selenium.Ejercicios_propuestos.Prueba_QA_18.Datos.dataWeb import dataWeb


class periodicos(dataWeb):

    def __init__(self):
        self.data = dataWeb

    def setNews(self, value='Marca'):
        self.dataNews['Prensa'] = value
        print(self.dataNews['Prensa'])

    def takeUrl(self):
        for c, v in self.dataNews.items():
            if c == self.dataNews['Prensa']:
                for c, v in v.items():
                    return v
            else:
                pass
