[Principal](../README.md)<br/>
[Api_Post](READMEPOST.md) | [Api_Get](READMEGET.md)  | [Tuplas](READMETupleSet.md) | [Listas](READMELIST.md) | [Diccionarios](READMEDIC.md) | [Selenium](../Selenium/README.md)
# API_Post:

    import requests

    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"Nombre": "Fer", "Edad": 39}
    response = requests.post(url, data, stream=True)
    print(response.status_code)
    response = response.json()
    print(response)

