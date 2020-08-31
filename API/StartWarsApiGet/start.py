import requests

response = requests.get("https://swapi.dev/api/vehicles/")
if response.status_code == 200:
    response = response.json()
    for c, v in response.items():
        if type(v) == list:
         for i in v:
           print(i)
