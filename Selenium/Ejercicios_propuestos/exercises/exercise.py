from Selenium.Ejercicios_propuestos.exercises.data import data
from Selenium.Ejercicios_propuestos.exercises.newspaper import newspaper


class exercise:
    # API
    # P1 = responses(Data.dataApiGet['url'], Data.dataApiGet['sospecha'])
    # P1.getApi()
    # P1.search()

    # newspaper
    P2 = newspaper(data.dataPaper)
    P2.setNews('Marca')
    P2.obtnUrl()
    P2.openUrl()

