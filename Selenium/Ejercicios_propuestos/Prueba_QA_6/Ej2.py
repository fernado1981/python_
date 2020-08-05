import requests

from Resp2 import Resp2


class Ej2:
    # API_GET
    url_Api = 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01'
    sospechoso = 'suspicious_car'
    color = 'pink'

    P2 = Resp2(url_Api, sospechoso)
    P2.obtData()
    P2.setColor('blue')
    P2.deleteColorList()
    P2.addlist(color)
    P2.addlist(color)
    P2.showList()
