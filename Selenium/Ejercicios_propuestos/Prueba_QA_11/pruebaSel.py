from Selenium.Ejercicios_propuestos.Prueba_QA_11.data import data
from Selenium.Ejercicios_propuestos.Prueba_QA_11.respSel import respSel


class pruebaSel:
    P1 = respSel(data.dataTelefonica)
    P1.openGoogle()
    P1.firstoption()
    P1.takeAllTag()
    P1.accpetBanner()
    P1.Accionistas()
    P1.valueNY()
    P1.TearDown()
