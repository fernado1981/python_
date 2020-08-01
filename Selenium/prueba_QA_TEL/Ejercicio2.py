from prueba_QA_TEL.Respuesta2 import Respuesta2


class Ejercicio2:
    url_api = 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01'
    sospechosos = 'suspicious_car'

    P2 = Respuesta2(url_api, sospechosos)
    P2.obtValueApi()
