from openlink import openlink


class newspaper:
    newsA = {"El Mundo": "https://www.elmundo.es/"}
    newsB = {"El Marca": "https://www.marca.com/"}

    lista = []
    lista.append(newsA)
    lista.append(newsB)

    link = openlink(lista)
    Url = link.obtUrl('El Mundo')
    link.opneUrl(Url)
    link.searchWord("LaLiga")
    link.clicktab("acuerdo histórico")

