from prueba_QA_TEL.Respuesta3 import Respuesta3


class Ejercicio3:
    urlGoogle = 'http://www.google.es'
    urlTelefonica = 'https://www.telefonica.com/es'
    inputGoogle = "input[name='q']"
    candidate_first_click = "//div[@id='search']//div[@class='g']"
    link = ".//a"

    P3=Respuesta3(urlGoogle,urlTelefonica,inputGoogle,candidate_first_click,link)
    P3.openGoogle()
    P3.firstCandidate()
    P3.obtTagHref()

