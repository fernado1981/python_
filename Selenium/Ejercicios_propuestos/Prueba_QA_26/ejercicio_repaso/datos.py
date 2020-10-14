from selenium import webdriver


class datos:
    drive = {'driver': webdriver.Chrome()}
    dts = {
        'pais': 'http://www.elpais.es',
        'marca': 'http://www.marca.es',
        'default': 'pais',
        'datos_post': {'nombre': 'Fernando'},
        'url_post': 'https://jsonplaceholder.typicode.com/posts'
    }

    dts_web = {
        'telefonica': 'https://www.telefonica.com/es',
        'cookie': '.cc-cookies #aceptar',
        'acciones': "//a[@title='Ir a Accionistas e inversores ']",
        # frame by_id
        'euroland': 'euroland-ticker-es',
        'NYSE': "//a[contains(.,'NYSE')]",
        'valny': '.LastCurrency'
    }
