from Accionista import Accionista


class Ejercicio4:
    url = 'https://www.telefonica.com/es'
    text = 'Accionistas e inversores'

    Ej4 = Accionista(url, text)
    Ej4.openUrl()
    Ej4.clickLink()
    Ej4.tearDown()
