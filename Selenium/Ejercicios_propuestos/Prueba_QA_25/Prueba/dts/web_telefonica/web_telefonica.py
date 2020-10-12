from selenium import webdriver


class web_telefonica:
    dt_web_telefonica = {
        # driver
        'driver': webdriver.Chrome(),
        # get
        'google': 'http://www.google.es',
        # input
        'igoogle': 'q',
        # send_key + key.ENTER
        'telefonioca': 'https://www.telefonica.com/es/',
        # first_option xpath .click()
        'first': "//div[@id='search']//div[@class='g']",
        # cssSelector .click()
        'cookie': '.cc-cookies #aceptar',
        # accionistas by_id .click()
        'acciones': "//a[@title='Ir a Accionistas e inversores ']",
        # frame switch_to.frame(frame)
        'frame': 'euroland-ticker-es',
        # NYSE .click()
        'NYSE': "//a[contains(.,'NYSE')]",
        # valNY (val.text)
        'valNY': '.LastCurrency'
    }

#crear clase con __init__(self) conctructor, pasarle los datos y el driver
#generar los diferentes metodos para cada acciónd e panatalla