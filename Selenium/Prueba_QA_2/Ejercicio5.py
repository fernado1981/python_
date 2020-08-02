from prueba_QA_TEL.Respuesta5 import respuesta5


class Ejercicio5:
    Bag = 'NYSE'
    iframe = 'euroland-ticker-es'
    values = '.Tab_Active .last'
    urlTelefonica = 'https://www.telefonica.com/es/web/shareholders-investors'

    P5 = respuesta5(urlTelefonica, Bag, values, iframe)
    P5.opnUrl()
    P5.obtValueNyse()
