[Principal](../README.md)<br/>
# Tuple set
    conjunto = ("pepe", "maria", "juanito", "raulin")
    conjuntos = {"pepe", "maria", "juanito", "raulin","fatima"}

> type
 
    print(type(conjunto))
    print(type(conjuntos))

> count and index en tuple, el set no lo permite
 
    print(conjunto.count("pepe"))
    print(conjunto.index("pepe"))

> transformar a conjunto set(conjunto)
 
    conjunto=set(conjunto)
    print(type(conjunto))

> funcionalidades del conjunto
  
    conjunto.remove("pepe")
    conjunto.pop()
    conjunto.discard("juanito")
    conjunto.update(conjuntos)
    print(conjunto.difference(conjuntos))
    conjunto.add("ramiro")
    print(len(conjunto))
    print(conjunto)

# Bucles asociados al conjunto
    for i in conjunto:
        print(i)

[Api_Post](API_post.md) | [Api_Get](API_Get.md)  | [Tuplas](READMETupleSet.md) | [Listas](READMELIST.md) | | [Diccionarios](READMEDIC.md) | [Selenium](../Selenium/README.md)