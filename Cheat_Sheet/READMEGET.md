[Principal](../README.md)<br/>

# IMPORT REQUESTS:

    import requests
    from pip._vendor import requests

# API_GET:
    
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
        print(lista)
     
     //response=['suspicious_car', ['black', 'blue']]
  
# API_POST:

    class ApiPrueba:
        url = "https://jsonplaceholder.typicode.com/posts"
        data = {"Nombre": "Fer", "Edad": 39}
        response = requests.post(url, data, stream=True)
        if response.status_code == 201:
            response = response.json()
        print(response)      

    // response = {'Edad': '39', 'id': 101, 'Nombre': 'Fer'}
