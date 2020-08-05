from Prueba_QA_.respuesta4 import respuesta4


class ejercicio4:
    ##open link accionistas
    Accionistas_link_text = "Accionistas e inversores"
    First_Option = "//div[@id='search']//div[@class='g']"
    Url_Google = 'http://www.google.es'
    key_word_Google = 'q'
    Url_Telefonica = 'https://www.telefonica.com/es'
    Iframe = 'euroland-ticker-es'
    NY = 'NYSE'
    Get_Data = '.Tab_Active .last'

    P4 = respuesta4(Accionistas_link_text, First_Option, Url_Google, key_word_Google, Url_Telefonica, Iframe, NY,
                    Get_Data)
    P4.openLink()
    P4.optionfirst()
    P4.obtainHref()
    P4.Accionist()
    P4.obtainvalueNy()
    P4.showList()
    P4.tearDown()