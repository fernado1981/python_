[Principal](../README.md)<br/>

# IMPORT REQUESTS:
    import requests
    from pip._vendor import requests

# API_GET:
    my_url = '<website>'
    response = requests.get(my_url)
    if response.status_code == 200:
       response = response.json()
       for c, v in response.items():
         print(c,v)
  
# API_GET_TOKEN:
    my_token = '<token>'
    my_url = '<website>'
    head = {'Authorization': 'token {}'.format(my_token)}
    response = requests.get(my_url, headers=head)
    if response.status_code==200:
       response = response.json()
       for c, v in response.items():
         print(c,v)
    
# API_GET_TOKEN_BEARER:  
    my_token = '<token>'
    my_url = '<website>'
    response = requests.get(my_url, headers={ 'Authorization': 'Bearer <my_token>' })
    if response.status_code==200:
       response = response.json()
       for c, v in response.items():
         print(c,v)
    
# API_GET_USER_PASS:
    my_url = '<website>'
    user = '<user>'
    pass = '<pass>'
    response = requests.get(my_url, auth=HTTPBasicAuth(user, pass))
    if response.status_code==200:
       response = response.json()
       for c, v in response.items():
         print(c,v)

# API_POST:
    my_url = '<website>'
    data = {"Nombre": user, "Edad": edad}
    response = requests.post(my_url, data, stream=True)
    if response.status_code == 201:
        response = response.json()
    print(response)      
