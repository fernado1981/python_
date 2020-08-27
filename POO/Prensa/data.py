from selenium import webdriver


class data:
    dataPrensa = {
        'Marca': {'url': 'http://www.marca.es'},
        'ElMundo': {'url': 'http://www.elmundo.es'},
        'default': 'Marca'
    }

    def openDriver():
        driver = webdriver.Chrome()
        driver.get(data.dataPrensa['url'])

