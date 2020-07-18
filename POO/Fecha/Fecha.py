from MostrarFecha import MostrarFecha


# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla
# la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

class Fecha:
    fecha = input("dame una fecha con el siguiente formato dd/mm/aaaa: ")
    fecha = fecha.split('/')

    ChFecha = MostrarFecha(fecha)
    ChFecha.cambioFecha()
