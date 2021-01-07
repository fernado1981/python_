[Principal](../README.md)<br/>

# IMPORT REQUESTS:
    import requests
    from pip._vendor import requests

# API_GET:
    my_url = '<website>'
    response = requests.get(url)
    if response.status_code == 200:
       response = response.json()
       for c, v in response.items():
         print(c,v)
  
# API_GET_TOKEN:
    my_token = '<token>'
    my_url = '<website>'
    head = {'Authorization': 'token {}'.format(my_token)}
    response = requests.get(my_url, headers=head)
    
# API_GET_TOKEN_BEARER:    
    response = requests.get('myurl', headers={ 'Authorization': 'Bearer <your_token>' })
    print response.json()
    
# API_GET_USER_PASS:
    from requests.auth import HTTPBasicAuth
    my_url = '<website>'
    user = '<user>'
    pass = '<pass>'
    requests.get(my_url, auth=HTTPBasicAuth(user, pass))

# API_POST:
    class ApiPrueba:
        url = "https://jsonplaceholder.typicode.com/posts"
        data = {"Nombre": "Fer", "Edad": 39}
        response = requests.post(url, data, stream=True)
        if response.status_code == 201:
            response = response.json()
        print(response)      

    // response = {'Edad': '39', 'id': 101, 'Nombre': 'Fer'}
