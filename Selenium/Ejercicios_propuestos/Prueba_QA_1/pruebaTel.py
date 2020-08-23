import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Selenium.TécnicaQA.ejercicios_prueba import ejercicio_prueba


class pruebaTel:
    Marca = {"url": "http://www.marca.es"}
    ElMundo = {"url": "http://elmundo.es"}
    Api_url = 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01'
    telefonica = 'https://www.telefonica.com/es/'
    lista = []
    periodicos = {"Marca": Marca, "ElMundo": ElMundo}

    # p1 = ejercicio_prueba(periodicos)
    # url = p1.showDiccionario()
    # p1.openUrl(url)
    # p1.setApi(Api_url)
    # p1.apiGetpy()
    # p1.searchTelefonica(telefonica)
    # p1.listadosTelefónica(telefonica)
    # p1.accionistas(telefonica)
    # p1.bolsaNYSE(telefonica)
