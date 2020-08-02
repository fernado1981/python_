from PruebaSelenium import PruebaSelenium


class Selenium:
    WebElement = "https://www.google.es"

    p = PruebaSelenium(WebElement)
    p.AbrirUrl()
    p.ObtenerTitleUrl()
    p.searchTelefonica()
    p.searchElements()
    p.Accionistas()
    p.NYSE_Values()
    p.tearDown()

