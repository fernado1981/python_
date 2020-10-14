import requests

from ejercicio_repaso.datos import datos


class periodicos(datos):

    def __init__(self):
        self.datos = self.dts
        self.driver = self.drive['driver']

    def open_url(self, val=''):
        if val == '':
            val = self.datos['default']
            for c, v in self.datos.items():
                if c == val:
                    self.datos['default'] = v
                    print(self.datos['default'])
                    self.driver.get(self.datos['default'])
        else:
            for c, v in self.datos.items():
                if c == val:
                    self.datos['default'] = v
                    print(self.datos['default'])
                    self.driver.get(self.datos['default'])

    def get_data(self):
        count = 0
        for val in self.driver.find_elements_by_xpath('.//a'):
            if val.get_attribute('href') is None:
                pass
            else:
                self.datos[count] = val.get_attribute('href')
                count += 1

    def post_data(self):
        response = requests.post(self.datos['url_post'], self.datos['datos_post'], stream=True)
        if response.status_code == 201:
            response = response.json()
            print(response)

    def close(self):
        self.driver.quit()

    def carga_arr(self):
        val = []
        for i in range(10):
            val.append(i)
        self.datos['val_arr'] = val

    def imprime(self, val='par'):
        if val == 'par':
            for c, v in self.datos.items():
                if c == 'val_arr':
                    for i in v:
                        if i % 2 == 0:
                            print(i)
        else:
            for c, v in self.datos.items():
                if c == 'val_arr':
                    for i in v:
                        if i % 2 != 0:
                            print(i)
