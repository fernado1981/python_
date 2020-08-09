from Selenium.Ejercicios_propuestos.Prueba_QA_10.ApiGet import ApiGet
from Selenium.Ejercicios_propuestos.Prueba_QA_10.data import data
from Selenium.Ejercicios_propuestos.Prueba_QA_10.playUrl import playUrl
from Selenium.Ejercicios_propuestos.Prueba_QA_10.valueNY import valueNY


class Ejercicio:
    P1 = ApiGet(data.dataApi)
    P1.GetApi()
    P1.showData()

    P2 = playUrl(data.dataPrensa)
    P2.setPrensa('ElMundo')
    P2.obtnUrl()
    P2.OpenUrl()
    P2.TearDown()

    P3 = valueNY(data.dataValueNY)
    P3.openUrl()
    P3.firstOption()
    P3.AceptBannerterms()
    P3.Acciones()
    P3.valueNY()
    P3.TearDown()
