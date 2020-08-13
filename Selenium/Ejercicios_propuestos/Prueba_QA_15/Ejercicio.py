from Core import Core


class Ejercicio():
    P1 = Core()
    P1.setNews('ElMundo')
    url = P1.getUrl()
    P1.__enter__(url)
    P1.__exit__()

    P2 = Core()
    P2.getData()
    P2.search()
    P2.showData()
    P2.__exit__()

    P3 = Core()
    P3.__enter__()
    P3.searchGoogle()
    P3.firstOption()
    P3.Banner()
    P3.takeTag()
    P3.Accionistas()
    P3.valNY()
    P3.__exit__()
