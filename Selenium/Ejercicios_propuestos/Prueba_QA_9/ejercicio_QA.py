from Selenium.Ejercicios_propuestos.Prueba_QA_9.Respuesta_QA import RespuestaQA


class ejercicioQA:
    Madrid = {"url": "http://www.realmadrid.es"}
    Barcelona = {"url": "http://www.fcbarcelona.es"}

    Equips = {"Madrid": Madrid['url'], "Barcelona": Barcelona['url']}

    P1 = RespuestaQA(Equips)
    P1.obtnUrl()
    P1.openUrl()
    P1.openGoogle()
    P1.buscar()
    P1.takeFirstoption()
    P1.takeAttributetag()
    P1.Accionistas()
    P1.popUpDown()
    P1.obtnNYValue()
    P1.TearDown()
