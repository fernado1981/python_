from selenium import webdriver


class data:
    driver = webdriver.Chrome()
    dataApi = {
        'url': 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01',
        'search': 'suspicious_car',
        'url1': 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_02',
        'search1': 'parkings',
        'url2': 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_03',
        'url3': 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_04'
    }

    dataNews = {
        'Marca': {'url': 'http://www.marca.es'},
        'ElMundo': {'url': 'http://www.elmundo.es'},
        'periodico': 'Marca'
    }

    dataExercise = {
        'getGoogle': 'http://www.google.es',
        'iGoogleName': 'q',
        'sendUrlTel': 'https://www.telefonica.com/es',
        'firstOptionXpath': "//div[@id='search']//div[@class='g']",
        'link': './/a',
        'BannerCss': '.cc-cookies .cc-cookie-accept',
        'AccionistaslinkText': 'Accionistas e inversores',
        'iframeId': 'euroland-ticker-es',
        'nyseLinkText': 'NYSE',
        'valNYCss': '.Tab_Active .last'
    }
