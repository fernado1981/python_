from Selenium.Ejercicios_propuestos.Prueba_QA_24.Telefonica_api import Telefonica_api


class launch:

    lanza = Telefonica_api()
    #lanza.get_api()
    #lanza.post_data()
    #lanza.change_to_dict()
    #lanza.imprimir_datos()
    #lanza.open_url('marca')

    lanza.sel_tel()
    lanza.cookie()
    lanza.accionistas_inversores()
    lanza.switch_frame()
    lanza.NYSE()
    lanza.valNy()
    lanza.close()


