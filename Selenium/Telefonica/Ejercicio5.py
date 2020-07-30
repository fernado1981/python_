from BolsaNY import BolsaNY


class Ejercicio5:
    url = 'https://www.telefonica.com/es/web/shareholders-investors'
    text_link = 'NYSE'
    iframeid = 'euroland-ticker-es'
    value = ".Tab_Active .last"

    Ej5 = BolsaNY(url, text_link, iframeid, value)
    Ej5.openUrl()
    Ej5.iframeBolsa()
    Ej5.obtNYBolsa()
    Ej5.tearDown()
