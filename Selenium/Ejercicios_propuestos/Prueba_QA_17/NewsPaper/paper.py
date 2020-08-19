from Selenium.Ejercicios_propuestos.Prueba_QA_17.Data.data import data


class paper(data):

    def __init__(self):
        self.data = data

    def setNews(self, item='Marca'):
        print(item)
        if item == 'Marca':
            self.dataNews['url'] = self.dataNews[item]['url']
        elif item == 'ElMundo':
            self.dataNews['url'] = self.dataNews[item]['url']
        else:
            pass

    def obtnUrl(self):
        print(self.dataNews['url'])
        return self.data.dataNews['url']
