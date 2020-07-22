import requests

from API.Post.Post import Post


class Post:
    # post filtrado por title y userId:1
    data = {'title': 'Pyton Requests', 'body': 'Requests are qwesome', 'userId': '1', 'id': 101}
    url = 'https://jsonplaceholder.typicode.com/posts'
    jsonExpected = {'title': 'Pyton Requests', 'body': 'Requests are qwesome', 'userId': '1', 'id': 101}
    responsePost = Post(url, jsonExpected, data)
    responsePost.postApi()
    responsePost.deleteValue('id')
    responsePost.comparation()
    responsePost.showResult()
