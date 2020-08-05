from Resp1 import resp1


class Ej1:
    Marca = {"url": "http://www.marca.es"}
    ElMundo = {"url": "http://www.elmundo.es"}

    Periodicos = {"Marca": Marca['url'], "ElMundo": ElMundo['url']}

    P1 = resp1(Periodicos)
    #P1.setMarca('ElMundo')
    P1.obtUrl()

