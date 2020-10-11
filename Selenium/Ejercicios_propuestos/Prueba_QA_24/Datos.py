from selenium import webdriver


class Datos:
    dats_api = {
        'drive': webdriver.Chrome(),
        'url_get': 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01',
        'url_post': 'https://jsonplaceholder.typicode.com/posts',
        'search_word': 'suspicious_car',
        'marca': 'http://www.marca.es',
        'pais': 'http://www.elpais.es',
        'url_default': 'marca'
    }

    dats_web = {
        # get
        'telefonica': 'https://www.telefonica.com/es',
        # xpath
        'Nyse': "//a[contains(.,'NYSE')]",
        'accionistas': "//a[@title='Ir a Accionistas e inversores ']",
        # 'first_option': "//div[@id='search']//div[@class='g']",
        # cssSelector .click
        'valNy': '.Tab_Active .last',
        'cookie': '.cc-cookies #aceptar',
        # frame
        'bolsa': 'euroland-ticker-es',
    }
