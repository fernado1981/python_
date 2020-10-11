from Prueba.Prensa import Prensa
from Prueba.Telefonica import Telefonica
from Prueba.selenium_tel import selenium_tel


class Lanzador():
    #tel = Telefonica()
    #tel.get_api()
    #tel.post_api({'nombre':'Fernando'})
    #tel.imprimir_datos()

    #tel = Prensa()
    #tel.periodico('marca')

    tel = selenium_tel()
    tel.open_web()
    tel.cookie()
    tel.accionistas()
    tel.change_frame()
    tel.NYse()
    tel.valNY()
    tel.close()

