import requests


class ApiPrueba:
    url = "http://demo5977139.mockable.io/qa-cdco/exercises/cars_01"
    sospechoso = 'suspicious_car'
    lista = []
    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
        for c, v in response.items():
            if c == sospechoso:
                lista.append(c)
                lista.append(v)

    for i in range(len(lista)):
        if type(lista[i]) == list:
            for i in range(len(lista[i])):
                if 'blue' in lista[i]:
                    print(True)
    print(lista[::-1])

    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"Nombre": "Fer", "Edad": 39}
    response = requests.post(url, data, stream=True)
    if response.status_code == 201:
        response = response.json()
    print(len(response))

