[Principal](../README.md)<br/>
# Diccionarios:

    Fernando = {"Nombre": "Fernando", "Apellidos": "Manrique", "Edad": 39}
    Diego = {"Nombre": "Diego", "Apellidos": "Manrique", "Edad": 27}
    alumnos = {'Fernando': Fernando, 'Diego': Diego}

    print(alumnos.keys())
    print(alumnos.values())
    print(alumnos['Fernando'].get("Nombre"))
    print(alumnos['Fernando']['Nombre'])
    alumnos['Fernando'].pop('Edad')
    alumnos['Fernando']['Rango'] = 'Faraón'
    print("tengo: ", alumnos)

    for c, v in alumnos.items():
        if c == "Diego":
            for i in v:
                print(i, ':', v[i])

[Api_Post](API_post.md) | [Api_Get](API_Get.md)  | [set_conjuntos](set_conjunto.md) | [lista_array](lista_Array.md) | [Selenium](../Selenium/README.md)