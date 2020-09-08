[Principal](../README.md)<br/>
[Api_Post](READMEPOST.md) | [Api_Get](READMEGET.md)  | [Tuplas](READMETupleSet.md) | [Listas](READMELIST.md) | [Diccionarios](READMEDIC.md) | [Selenium](../Selenium/README.md)<br/>
# API_Get:


... from pip._vendor import requests
... class ApiPrueba:
...    url = "http://demo5977139.mockable.io/qa-cdco/exercises/cars_01"
...    sospechoso = 'suspicious_car'
...    lista = []
...    response = requests.get(url)
...    if response.status_code == 200:
...        response = response.json()
...        for c, v in response.items():
...            if c == sospechoso:
...                lista.append(c)
...                lista.append(v)
...   print(lista)       
