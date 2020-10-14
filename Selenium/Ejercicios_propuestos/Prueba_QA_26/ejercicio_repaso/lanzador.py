from ejercicio_repaso.periodicos import periodicos
from ejercicio_repaso.web import web


class lanzador:

    #lanza=periodicos()
    #lanza.open_url('marca')
    #lanza.get_data()
    #lanza.close()
    #lanza.post_data()
    #lanza.carga_arr()
    #lanza.imprime('impar')

    lanza=web()
    lanza.open_url()
    lanza.cookie()
    lanza.acciones()
    lanza.euro()
    lanza.nyse()
    lanza.take_val()

    lanza = periodicos()
    lanza.close()