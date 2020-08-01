from prueba_QA_TEL.Respuesta1 import Respuesta1


class Ejercicio1:
    Marca = {"url": "http://www.marca.es"}
    ElMundo = {"url": "http://www.elmundo.es"}

    Periodicos = {"Marca": Marca['url'], "ElMundo": ElMundo['url']}

    print(Periodicos)

    P1=Respuesta1(Periodicos)
    P1.setmarca("ElMundo")
    P1.obtMarca()
    
