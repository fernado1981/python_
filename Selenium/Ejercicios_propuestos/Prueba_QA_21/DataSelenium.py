from selenium import webdriver


class DataSelenium:
    data = {
        'driver': webdriver.Chrome(),
        # abrimos url get
        'google': 'http://www.google.es',
        # buscamos el input by_name
        'iGoogle': 'q',
        # escribimos en el input send_key
        'iTelco': 'https://www.telefonica.com/es',
        # buscamos por xpath
        'first': "//div[@id='search']//div[@class='g']",
        'link': './/a',
        'tag': 'href',
        'NYSE': "//a[contains(.,'NYSE')]",
        # buscamos por css-selector
        'cookie': '.cc-cookies .cc-cookie-accept',
        'valNY': '.Tab_Active .last',
        # buscamos por by_link_text
        'Acciones': 'Accionistas e inversores',
        # buscamos por by_id
        'iframe': 'euroland-ticker-es',
    }