from Selenium.linkedin import linkedin


class initLinkedin:
    User = "fernando.manrique.villanueva@gmail.com"
    Passwd = "Bimbo2020"
    Url = "http://www.google.es"

    opensesion = linkedin(Url, User, Passwd)
    opensesion.serachUrl()
    opensesion.initSesion()
    opensesion.quitdriver()
