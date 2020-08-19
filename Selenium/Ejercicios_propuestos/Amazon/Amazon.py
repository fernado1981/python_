from Selenium.Ejercicios_propuestos.Amazon.pruebaAmazon import pruebaAmazon


class Amazon:
    urlGoogle = 'http://www.google.es'
    KeyWordGoogle = 'q'
    SearchAmazon = 'amazon'
    searchFirstoption = "//div[@id='search']//div[@class='g']"
    AcceptCookie = '.a-declarative .sp-cc-buttons .a-button-primary'
    inputAmazon = '.nav-search-field  #twotabsearchtextbox'
    buscar = 'abrigos nepal hombre'
    index = "//img[@Data-image-index=30]"

    PAmazon = pruebaAmazon(urlGoogle, KeyWordGoogle, SearchAmazon, searchFirstoption, AcceptCookie, inputAmazon)
    PAmazon.OpenAmazon()
    PAmazon.searchChoose(buscar)
    PAmazon.obtData()
    PAmazon.selecionarPrenda(index)
