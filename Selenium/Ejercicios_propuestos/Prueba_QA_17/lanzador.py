from Selenium.Ejercicios_propuestos.Prueba_QA_17.Api.getApi import getApi
from Selenium.Ejercicios_propuestos.Prueba_QA_17.NewsPaper.paper import paper
from Selenium.Ejercicios_propuestos.Prueba_QA_17.Teleco.teleco import teleco


class lanzador:
    # P1 = getApi()
    # P1.getData()
    # P1.searchData()
    # P1.showData()

    # P2 = paper()
    # P2.setNews()
    # url = P2.obtnUrl()
    # P2.openUrl(url)
    # P2.tearDown()

    P3 = teleco()
    P3.openUrl('Google')
    P3.firstOption()
    P3.cookie()
    P3.tagRef()
    P3.Acciones()
    P3.valueNY()
    P3.tearDown()
