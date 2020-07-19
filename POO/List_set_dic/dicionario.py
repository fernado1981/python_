from List_set_dic.dictionary import dictionary


class dicionario:
    dicA = {"jefe": {"Nombre": "fernando", "Apellidos": "Manrique villanueva", "Edad": 39}}
    dicB = {"pipiolo": {"Nombre": "diego", "Apellidos": "Manrique villanueva", "Edad": 27}}
    lista = []
    lista = [dicA] + [dicB]

    dic = dictionary(lista, dicA, dicB)
    dic.addkey()
    dic.aroundDict()
    dic.arounDictAdd("Range", "bombardier")
    dic.deleteBKeyValue("Apellidos")
