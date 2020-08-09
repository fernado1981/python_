from Selenium.Ejercicios_propuestos.Prueba_QA_11.data import data
from Selenium.Ejercicios_propuestos.Prueba_QA_11.respuesta import respuesta


class Pruebas:
    # Api con variables
    # url = 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_02'
    # sospechoso = 'suspicious_parkings'

    # P1 = Respuestas(url, sospechoso)
    # P1.getApi()
    # P1.search()

    # Api con diccionario toma los datos de un fichero externo
    P1 = respuesta(data.dataApi)
    P1.getApi()
    P1.search()
