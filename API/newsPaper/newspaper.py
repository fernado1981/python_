from API.newsPaper.prueba import paper


class newspaper:
    periodicoA = {"url": "https://www.elmundo.es"}
    periodicoB = {"url": "https://www.marca.com/"}
    periodicoC = {"url": "https://jsonplaceholder.typicode.com/posts/"}
    periodicos = {'El mundo': periodicoA, 'Marca': periodicoB, 'PruebaApi': periodicoC}

    data = {"Nombre": "Fernando", "Edad": 39}

    news = paper(periodicos, periodicoC['url'])
    url = news.urlNews('Marca')
    news.openUrl(url)
    news.ApiGet()
    news.ApiPost(data)
    news.ApiPut(data)
    news.ApiDel()
    news.quitDriver()
