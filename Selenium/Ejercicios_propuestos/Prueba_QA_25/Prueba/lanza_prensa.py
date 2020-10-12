from Prueba.prensa.prensa import prensa


class lanza_prensa:
    lanza = prensa()
    lanza.open_url('marca')
    lanza.close()
