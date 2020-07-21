from API.PostPrueba.PostData import postData


class ApiPostyPrueba:
    data = {"Nombre": "Fernando", "Edad": 39}

    url = 'https://jsonplaceholder.typicode.com/posts'
    Add = postData(url, data)
    Add.AddData()
