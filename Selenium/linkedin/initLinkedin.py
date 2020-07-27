from Selenium.linkedin.linkedin import Testlinkedin


class initLinkedin:
    User = "fernando.manrique.villanueva@gmail.com"
    Passwd = "*******"
    Url = "http://www.google.es"

    sesion = Testlinkedin(Url, User, Passwd)
    sesion.serachUrl()
    sesion.initSesion()
    sesion.logout()
    sesion.quitdriver()
