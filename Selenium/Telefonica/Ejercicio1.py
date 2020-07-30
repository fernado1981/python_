from newspaper import newspaper


class Ejercicio1:
    # dado un diccionario de marca de periodico y url, pasarlo al contructor y abriren selenium el periodico deseado

    Marca = {"url": "http://www.marca.es"}
    ElMundo = {"url": "http://www.elmundo.es"}

    periodicos = {"Marca": Marca, "ElMundo": ElMundo}

    p1 = newspaper(periodicos)
    p1.setnews("Marca")
    p1.obtenerUrl()
    p1.tearDown()
