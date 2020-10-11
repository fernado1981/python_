import requests

from Selenium.Ejercicios_propuestos.Prueba_QA_24.Datos import Datos


class Telefonica_api(Datos):

    def __init__(self):
        self.Ds_url_get = Datos.dats_api['url_get']
        self.Ds_url_post = Datos.dats_api['url_post']
        self.Ds_search = Datos.dats_api['search_word']
        self.DS_url = Datos.dats_api['url_default']
        self.driver = Datos.dats_api['drive']
        self.DS_web = Datos.dats_web

    def get_api(self):
        self.response = requests.get(self.Ds_url_get)

        if self.response.status_code == 200:
            self.response = self.response.json()
            for c, v in self.response.items():
                if c == self.Ds_search:
                    Datos.dats_api['search'] = True
                    Datos.dats_api['suspicious_value'] = v

    def imprimir_datos(self):
        for c, v in self.dats_api.items():
            print(type(v))
            if c == 'url_get' or c == 'url_post':
                pass
            else:
                print(c, v)

    def post_data(self, val={'nombre': 'fernando'}):
        response = requests.post(self.Ds_url_post, val, stream=True)
        if response.status_code == 201:
            response = response.json()
            print(response)

    def change_to_dict(self):
        count = 0
        for c, v in self.dats_api.items():
            if type(v) == list:
                for item in v:
                    print(count)
                    self.dats_api[count] = {c: item}
                    count += 1
                break

    def open_url(self, default=''):
        if default == '':
            for c, v in self.dats_api.items():
                if c == self.DS_url:
                    self.driver.get(v)
                    break
        else:
            for c, v in self.dats_api.items():
                if c == default:
                    self.driver.get(v)
                    break

    def sel_tel(self):
        self.driver.get(self.dats_web['telefonica'])
        self.driver.implicitly_wait(5)

    def cookie(self):
        self.driver.find_element_by_css_selector(self.dats_web['cookie']).click()
        self.driver.implicitly_wait(5)

    def accionistas_inversores(self):
        self.driver.find_element_by_xpath(self.dats_web['accionistas']).click()
        self.driver.implicitly_wait(5)

    def switch_frame(self):
        self.driver.maximize_window()
        frame = self.driver.find_element_by_id(self.dats_web['bolsa'])
        self.driver.switch_to.frame(frame)

    def NYSE(self):
        self.driver.find_element_by_xpath(self.dats_web['Nyse']).click()
        self.driver.implicitly_wait(5)

    def valNy(self):
        for val in self.driver.find_elements_by_css_selector(self.dats_web['valNy']):
            print(val.text)

        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()
