from Selenium.Ejercicios_propuestos.Prueba_QA_12.ApiGet import ApiGet
from Selenium.Ejercicios_propuestos.Prueba_QA_12.data import data
from Selenium.Ejercicios_propuestos.Prueba_QA_12.Prensa import Prensa
from Selenium.Ejercicios_propuestos.Prueba_QA_12.exerciseTest import exerciseTest


class ejercicio:
    #P1 = Prensa(Data.dataNews)
    # P1.setNew('ElMundo')
    # P1.obtnUrl()
    # P1.openUrl()
    # P1.tearDown()

    # P2 = ApiGet(Data.dataApi)
    # P2.obtData()
    # P2.search()

    P3 = exerciseTest(data.exercise)
    P3.openNavigator()
    P3.firstOption()
    P3.AcceptBanner()
    P3.Accionistas()
    P3.valueNY()
    P3.tearDown()
