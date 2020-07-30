from suspicious import suspicious


class Ejercicio2:
#dada una url de una api extraer los datos en una lista, buscar el dato sospechosos y volcarlo en la lista
    api_url='http://demo5977139.mockable.io/qa-cdco/exercises/cars_01'

    api1 = suspicious(api_url)
    api1.getdata()
    api1.showLista()
