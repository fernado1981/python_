import requests

from Get import Get
#obtener los datos de una Url con get parsarlos a json , y esperar que sean iguales a los deseados

class get:
    # declaramos nuestro diccionario expected
    ExpectedJson = {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
    # get del listado filtrado por UserId:1
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    #hacemos la peticion get pasandole la url
    response = requests.get(url)
    #imprimimos el status
    print(response.status_code)
    #parseamos a json la response
    responseJson = response.json()
    #creamos un objeto de tipo Get y la pasamor el responseJson y el ExpectedJson al constructor
    Param = Get(responseJson, ExpectedJson)
    #invocamosd al método comparation de Get
    Param.comparation()
    #Añadimos valores al dic obtenido
    Param.addValue('Name', 'Fernando')
    #Mostramos resultados
    Param.showResult()
    #Eliminamod valores del diccionario
    Param.deleteValue('Name', 'Fernando')
    #Mostramos valores
    Param.showResult()
