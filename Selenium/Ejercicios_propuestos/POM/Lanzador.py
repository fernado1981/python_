from Selenium.Ejercicios_propuestos.POM.Pages.TelefonicaAcciones import TelefonicaAcciones
from Selenium.Ejercicios_propuestos.POM.Pages.TelefonicaHome import TelefonicaHome
from Selenium.Ejercicios_propuestos.POM.hook.SeleniumTest import SeleniumTest


class lanzador:
    p = SeleniumTest()
    p.OpenBrowser()
    p.firstOpt()

    TelefHome = TelefonicaHome()
    TelefHome.TakeTag()
    TelefHome.Cookie()
    TelefHome.Acciones()

    TelfAcciones=TelefonicaAcciones()
    TelfAcciones.Euroland()
    TelfAcciones.NySe()
    TelfAcciones.valNY()

    p.closeBrowser()
