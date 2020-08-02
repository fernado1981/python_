from prueba_QA_TEL.Respuesta3 import Respuesta3
from prueba_QA_TEL.Respuesta4 import Respuesta4


class Ejercicio4:
    Accionistas = "Accionistas e inversores"
    urlTelefonica = 'https://www.telefonica.com/es'

    p4 = Respuesta4(urlTelefonica,Accionistas)
    p4.openAccionista()
