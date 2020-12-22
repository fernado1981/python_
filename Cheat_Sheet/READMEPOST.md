[Principal](../README.md)<br/>

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
    
    

