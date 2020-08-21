from Selenium.Ejercicios_propuestos.Prueba_QA_18.Api.apiGet import apiGet
from Selenium.Ejercicios_propuestos.Prueba_QA_18.NewsPaper.periodicos import periodicos
from Selenium.Ejercicios_propuestos.Prueba_QA_18.Teleco.telefonica import telefonica


class eject:
    #p1 = apiGet()
    #value = p1.getdata()
    #p1.searchdata(value)
    #p1.showData()

   #p2 = periodicos()
   #p2.setNews('ElMundo')
   #url = p2.takeUrl()
   #p2.openUrl(url)
   #p2.exit()

    P3 = telefonica()
    P3.openUrl()
    P3.inputName()
    P3.firstOption()
    P3.cookie()
    P3.takeTag()
    P3.acciones()
    P3.switchFrame()
    P3.changeValueNY()
    P3.getValueNY()
    P3.exit()
