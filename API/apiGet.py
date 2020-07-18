import requests

from Get import Get


class get:
    # api-endpoint
    # get del listado
    # url = 'https://jsonplaceholder.typicode.com/todos/'
    # response = requests.get(url)  # To execute get request
    # print(response.status_code)  # To print http response code
    # jsonRes = response.json()

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


# post del listado
# response = requests.post('https://jsonplaceholder.typicode.com/posts', data=None)
# jsonRes = response.json()  # output: {'id': 101}
# print(response.status_code)
# print(jsonRes)

# post filtrado por title y userId:1
# data = {'title': 'Pyton Requests', 'body': 'Requests are qwesome', 'userId': 1}
# response = requests.post('https://jsonplaceholder.typicode.com/posts', data, stream=True)
# jsonRes = response.json()
# print(response.status_code)
# print(jsonRes['title'], jsonRes['body'], sep=' : ')
