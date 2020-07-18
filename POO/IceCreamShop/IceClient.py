from IceCreamShop import IceCreamShop


class IceClient:
    helados = {"nombre": "Mango", "precio": 1.50, "refresco": "cola", "precioBebida": 2.50}
    heladosA = {"nombre": "Fresa", "precio": 3.50, "refresco": "pina", "precioBebida": 3.50}
    heladosB = {"nombre": "Nata", "precio": 2.50, "refresco": "fanta", "precioBebida": 2.50}

    lista = [helados] + [heladosA] + [heladosB]

    client = IceCreamShop(lista)
    client.verLista()
    client.helado()
    client.bebida()
    client.cuenta()