from Selenium.Ejercicios_propuestos.prueba_QA_13.Respuestas import Respuestas
from Selenium.Ejercicios_propuestos.prueba_QA_13.data import data


class Ejercicios:
    #P1 = Respuestas(Data)
    #P1.getdata()
    #P1.busca()
    #P1.showData()

    #P2 = Respuestas(Data)
    #P2.setNew()
    #P2.getUrl()
    #P2.openUrl()
    #P2.tearDown()

    P3 = Respuestas(data)
    P3.openGoogle()
    P3.firstOption()
    P3.AccepBaner()
    P3.takeTag()
    P3.Accionistas()
    P3.valueNY()
    P3.tearDown()
