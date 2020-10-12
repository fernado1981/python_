from Prueba.dts.Prensa.data_prensa import data_prensa


class prensa(data_prensa):

    def __init__(self):
        self.data = self.dt_prensa
        self.driver = self.dt_prensa['driver']

    def open_url(self, val=''):
        if val == '':
            val = self.data['default']
            for c, v in self.data.items():
                if c == val:
                    self.driver.get(v)
        else:
            for c, v in self.data.items():
                if c == val:
                    self.driver.get(v)

    def close(self):
        self.driver.quit()
