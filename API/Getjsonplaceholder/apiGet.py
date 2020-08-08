from Get import Get

class get:
    # declaramos nuestro diccionario expected
    ExpectedJson = {'userId': 1, 'id': 1, 'title': 'delectus aut autem','completed': False}
    # get del listado filtrado por UserId:1
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    #creamos un objeto de tipo Getjsonplaceholder y la pasamor el responseJson y el ExpectedJson al constructor
    Param = Get(url, ExpectedJson)
    #invocamos el get de la url
    Param.obtGet()
    #invocamos al método comparation de Getjsonplaceholder
    Param.comparation()
    #Añadimos valores al dic obtenido
    Param.addValue('Name', 'Fernando')
    #Mostramos resultados
    Param.showResult()
    #Eliminamos valores del diccionario
    Param.deleteValue('Name', 'Fernando')
    #Mostramos valores
    Param.showResult()
