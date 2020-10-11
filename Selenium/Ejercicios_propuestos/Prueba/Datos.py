from selenium import webdriver


class Datos:
    datos_Driver = {'drive': webdriver.Chrome()}
    datos_Api = {
        'url_get': 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01',
        'url_post': 'https://jsonplaceholder.typicode.com/posts',
        'search_word': 'suspicious_car'
    }

    datos_url = {
        'marca': 'http://www.marca.es',
        'pais': 'http://www.elpais.es',
        'default': 'pais'
    }

    datos_web = {
        # get
        'telefonica': 'https://www.telefonica.com/es',
        # cssSelector
        'valNy': '.Tab_Active .last',
        'cookie': '.cc-cookies #aceptar',
        # xpath accionistas
        'accionista': "//a[@title='Ir a Accionistas e inversores ']",
        'NYSE': "//a[contains(.,'NYSE')]",
        # by_ID
        'frame': 'euroland-ticker-es',
    }
