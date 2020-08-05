from selenium3 import selenium3


class Ejercicio3:
    # abrir google, introducir https://www.telefonica.com/es, haciendo click en la primera aparición del buscador

    url = "http://www.google.es"
    url_search = 'https://www.telefonica.com/es'

    Ej3 = selenium3(url, url_search)
    Ej3.openGoogle()
    Ej3.obtTags()
    Ej3.tearDown()
