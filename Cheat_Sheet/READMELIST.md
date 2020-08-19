[Principal](../README.md)<br/>
[Api_Post](READMEPOST.md) | [Api_Get](READMEGET.md)  | [Tuplas](READMETupleSet.md) | [Listas](READMELIST.md) | [Diccionarios](READMEDIC.md) | [Selenium](../Selenium/README.md)
# lista/array
    lista = [1, 2, 3, "hola", [4, 6, 2], {"Nombre:""Fernando"}, ("paco", "maria")]
> append para añadir lista.append(valor)

    lista.append("rambo")

> insert para insertar un valor en un a posición determinada lista.insert(posicion,valor)

    lista.insert(2, "pepe")

> remove para eliminar un valor lista.remove(valor)

    lista.remove(3)

> pop eliminamos la ultima posición lista.pop()

    lista.pop()

> del para eliminar posicion del lista[posicion]

    del lista[0]
> pop por posicion lista.pop(1)

    lista.pop(1)

> index para buscar una posicion lista.index(valor)

    print(lista.index("hola"))

> sort() para ordenar lista.sort()

    lista[2].sort()
    
>  Ordenar la lista de objetos usando un parámetro "clave"
        
    myArray = [{"name": "Mario Peres"}, {"name": "Emilio Peres"}, {"name": "Yusaiba Peres"}]
    myArray.sort(key=lambda person: person['name'])
    print(myArray)

> count para contar elementos de una lista lista.count(v)

    print(lista.count("hola"))

> len para ver el tamaño de la lista len(lista)

    print(len(lista))

# Bucles asociados al array

    for i in lista:
        print(i)

    for i in range(len(lista)):
        print(lista[i])

> recorrer la lista dentro del array
 
    for i in range(len(lista)):
        if type(lista[i]) == list:
            for i in lista[i]:
                print(i)

> recorrer diccionario dentro del array

    for i in range(len(lista)):
        if type(lista[i]) == dict:
            for c, v in lista[i].items():
                print(c, v)
            
    for i in lista:
        if type(i) == dict:
            print(i['Nombre'])
