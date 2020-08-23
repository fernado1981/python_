from selenium import webdriver


class data:
    driver = webdriver.Chrome()
    news = {
        'Marca': {'url': 'http://www.marca.es'},
        'ElMundo': {'url': 'http://www.elmundo.es'},
        'prensaDefault': 'Marca',
        'url': 'http://www.marca.es'
    }
