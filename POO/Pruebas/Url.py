from ObtUrl import ObtUrl


class Url:
    Marca = {"Url": "http://www.marca.es"}
    Madrid = {"Url": "http://www.realmadrid.com"}

    prensa = {"Marca": Marca['Url'], "Madrid": Madrid['Url']}

    P1 = ObtUrl(prensa)
    P1.setPeriodico('Madrid')
    P1.obtnUrl()

