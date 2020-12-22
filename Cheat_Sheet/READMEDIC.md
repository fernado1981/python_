<a name="top"></a>
[Principal](../README.md)<br/>

# cramos el diciconario {K,V}
    Fernando = {"Apellidos": "manrique villanueva", "Edad": 39, "Profesión": "Informático"}
    Diego = {"Apellidos": "manrique villanueva", "Edad": 39, "Profesión": "Informático"}
    dicF = {"Fernando": Fernando, "Diego": Diego}

- type dic
    
        print(type(dicF))

# funcionaes del diccionario
- add -- añadir
  
      dicF['Fernando']["Rango"] = "Rambo"
    
- pop(v) -- Eliminar por valor

      dicF['Fernando'].pop('Edad')

- values -- ver valores

      print(dicF.values())

- keys -- ver claves

      print(dicF.keys())

- len  -- longitud

      print(len(dicF))

# Bucles asociados al diccionario
    for c, v in dicF.items():
        if c == "Fernando":
            for c,v in v.items():
                print(c,v)

    for c, v in Diego.items():
        print(c,v)
        
[Subir](#top)
