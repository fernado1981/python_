from Prueba.Datos import Datos


class Prensa(Datos):

    def __init__(self):
        self.driver = self.datos_Driver['drive']

    def periodico(self, url=Datos.datos_url['default']):
        if url == self.datos_url['pais']:
            self.driver.get(url)
        elif url == self.datos_url['marca']:
            self.driver.get(url)
        else:
            for c, v in self.datos_url.items():
                if c == url:
                    self.driver.get(v)
