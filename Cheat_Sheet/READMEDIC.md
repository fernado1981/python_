[Principal](../README.md)<br/>
# cramos el diciconario {K,V}
    Fernando = {"Apellidos": "manrique villanueva", "Edad": 39, "Profesión": "Informático"}
    Diego = {"Apellidos": "manrique villanueva", "Edad": 39, "Profesión": "Informático"}
    dicF = {"Fernando": Fernando, "Diego": Diego}

# type dic
    print(type(dicF))

# funcionaes del diccionario
> add
  
    dicF['Fernando']["Rango"] = "Rambo"

> values

    print(dicF.values())

> keys

    print(dicF.keys())

> len

    print(len(dicF))

# Bucles asociados al diccionario
    for c, v in dicF.items():
        if c == "Fernando":
            for c,v in v.items():
                print(c,v)

    for c, v in Diego.items():
        print(c,v)
        
[Api_Post](API_post.md) | [Api_Get](API_Get.md)  | [Tuplas](READMETupleSet.md) | [Listas](READMELIST.md) | | [Diccionarios](READMEDIC.md) | [Selenium](../Selenium/README.md)