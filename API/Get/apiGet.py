import requests

from Get import Get
#obtener los datos de una Url con get parsarlos a json , y esperar que sean iguales a los deseados

class get:
    # get del listado filtrado por UserId:1
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(url)
    print(response.status_code)
    responseJson = response.json()
    print(responseJson)
    ExpectedJson = {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
    Param = Get(responseJson, ExpectedJson)
    Param.comparation()
    Param.addValue('Name', 'Fernando')
    Param.showResult()
    Param.deleteValue('Name', 'Fernando')
    Param.showResult()
