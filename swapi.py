import requests

response = requests.get('http://swapi.dev/api/planets')
if response.status_code == 200:
    response = response.json()

    for c, v in response.items():
        if type(v) == list:
            for item in v:
                    print(item['name'] == 'Tatooine')
