from Resp3 import Resp3


class Ej3:
    urlGoogle = 'http://www.google.es'
    inputNameGoogle = 'q'
    firstXpathOption = "//div[@id='search']//div[@class='g']"
    link = './/a'
    urlTelefonica = 'https://www.telefonica.com/es'

    P3 = Resp3(urlGoogle, inputNameGoogle, firstXpathOption, link, urlTelefonica)
    P3.openFirstoption()
    P3.obtDataRTag()
    P3.showData()
    P3.tearDown()
