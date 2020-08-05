from Resp4 import Resp4


class Ej4:
    urlTelefonica = 'https://www.telefonica.com/es'
    AccionesLink = 'Accionistas e inversores'
    iframe = 'euroland-ticker-es'
    NyseLink = 'NYSE'
    valuesByNy = '.Tab_Active .last'

    P4 = Resp4(urlTelefonica, AccionesLink, iframe, NyseLink, valuesByNy)
    P4.openUrl()
    P4.Acciones()
    P4.valuesNy()
    P4.terDown()
