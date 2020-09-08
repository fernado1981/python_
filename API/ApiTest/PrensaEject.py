from Api.Prensa import Prensa


class PrensaEject:
    data = {
        'Marca': {'url': 'http://www.marca.es'},
        'ElMundo': {'url': 'http://www.elmundo.es'},
        'default': 'Marca'
    }

    p = Prensa(data)
    p.setNews()
    p.searchUrl()
    p.openBrowser()
    p.closeBrowser()
