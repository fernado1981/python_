from Prueba_QA_.respuesta1 import respuesta1
from Prueba_QA_.respuesta2 import respuesta2
from Prueba_QA_.respuesta3 import respuesta3


class ejercicio1:
    ##Creacion de diccionarios y obtención de url
    marca = {"url": "http://www.marca.es"}
    elmundo = {"url": "http://www.elmundo.es"}
    periodico = {"marca": marca['url'], "elmundo": elmundo['url']}

    P1 = respuesta1(periodico)
    P1.setNew('Marca')
    P1.obtUrl()

    ##API_GET obtención de datos y busqueda del sospechosos
    url_Api = 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01'
    sospechosos = 'suspicious_car'

    P2 = respuesta2(url_Api, sospechosos)
    P2.ApiGet()
    P2.obtData()

    ##buscar en google telefonica.com/es y haz click sobre la primera opcion obtener el listado completo
    urlgetGoogle = 'http://www.google.es/'
    byNameGoogle = 'q'
    urlgetTel = 'https://www.telefonica.com/es'
    firstXpathOption = "//div[@id='search']//div[@class='g']"
    link ='.//a'

    P3 = respuesta3(urlgetGoogle, byNameGoogle, urlgetTel, firstXpathOption, link)
    P3.openNavigator()
    P3.searchFirstoption()
    P3.obtlistTag()

