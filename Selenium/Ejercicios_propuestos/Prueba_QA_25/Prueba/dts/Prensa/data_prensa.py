from selenium import webdriver


class data_prensa:
    dt_prensa = {
        'driver': webdriver.Chrome(),
        'pais': 'http://www.elpais.es',
        'marca': 'http://www.marca.es',
        'default': 'pais'
    }


#generar clase con contructor y pasarle los datos
#definir un metod en la clase que recoja el nombre y abra la url
