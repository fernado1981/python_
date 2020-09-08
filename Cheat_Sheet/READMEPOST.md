[Principal](../README.md)<br/>
[Api_Post](READMEPOST.md) | [Api_Get](READMEGET.md)  | [Tuplas](READMETupleSet.md) | [Listas](READMELIST.md) | [Diccionarios](READMEDIC.md) | [Selenium](../Selenium/README.md)
# API_Post:

    import requests
    
    class ApiPrueba:
        url = "https://jsonplaceholder.typicode.com/posts"
        data = {"Nombre": "Fer", "Edad": 39}
        response = requests.post(url, data, stream=True)
        if response.status_code == 201:
            response = response.json()
        print(response)      
    
    // response = {'Edad': '39', 'id': 101, 'Nombre': 'Fer'}
    
    

