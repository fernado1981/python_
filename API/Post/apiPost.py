import requests

from Post import Post


class Post:
    # post del listado
    # response = requests.post('https://jsonplaceholder.typicode.com/posts', data=None)
    # jsonRes = response.json()  # output: {'id': 101}
    # print(response.status_code)
    # print(jsonRes)

    # post filtrado por title y userId:1
    data = {'title': 'Pyton Requests', 'body': 'Requests are qwesome', 'userId': 1}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data, stream=True)
    print(response.status_code)
    jsonRes = response.json()
    jsonExpected = {'title': 'Pyton Requests', 'body': 'Requests are qwesome', 'userId': '1', 'id': 101}
    responsePost = Post(jsonRes, jsonExpected)
    responsePost.deleteValue('title', 'Pyton Requests')
    responsePost.addValue('title', 'Pyton Requests')
    responsePost.comparation()
    responsePost.showResult()
