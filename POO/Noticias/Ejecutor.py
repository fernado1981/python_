from POO.Noticias.Prensa import Prensa


class Ejecutor:

    p = Prensa()
    p.setNews()
    p.getUrl()
    p.openBrowser()
