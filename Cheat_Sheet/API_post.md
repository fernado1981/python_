[Principal](../README.md)<br/>
# API_Post:

    import requests

    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"Nombre": "Fer", "Edad": 39}
    response = requests.post(url, data, stream=True)
    print(response.status_code)
    response = response.json()
    print(response)

[Api_Get](API_Get.md) | [diccionario](diccionario.md) | [set_conjuntos](set_conjunto.md) | [lista_array](lista_Array.md) | [Selenium](../Selenium/README.md)