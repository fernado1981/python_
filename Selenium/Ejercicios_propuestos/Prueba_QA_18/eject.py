from Selenium.Ejercicios_propuestos.Prueba_QA_18.Api.apiGet import apiGet
from Selenium.Ejercicios_propuestos.Prueba_QA_18.NewsPaper.periodicos import periodicos


class eject:
    #p1 = apiGet()
    #value = p1.getdata()
    #p1.searchdata(value)
    #p1.showData()

   p2 = periodicos()
   p2.setNews('ElMundo')
   url = p2.takeUrl()
   p2.openUrl(url)
   p2.exit()
