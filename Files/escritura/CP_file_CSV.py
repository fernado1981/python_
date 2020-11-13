import csv

# inicializamos las variables con el csv que contien los datos y el que deseamos crear
import json

file_ori = '../asociacion.csv'
file_cp = '../asociacion_cp.csv'

# abrimos uno sólo de lectura el que contiene los datos y el vacio en modo escritura 'w'
with open(file_ori, encoding='latin1') as fitch_lect, open(file_cp, 'w', encoding='latin1') as fitch_esrc:
    # leemos el fichero con DictReader para que contenga la cabecera
    dict_lector = csv.DictReader(fitch_lect)
    # añadimos los nuevos campos en la cabecera
    campos = dict_lector.fieldnames + ['Justificacion requerida', 'justificacion recibida']
    escritor = csv.DictWriter(fitch_esrc, fieldnames=campos)
    escritor.writeheader()

    # iteracion con el objeto dict_lector
    for linea in dict_lector:
        # conertimos a float el importe y comprobamos si es mayor de 300
        if float(linea['Importe']) > 300:
            # si la condicion se cumple añade el valor 'Si' a la columna Justificacion requerida
            linea['Justificacion requerida'] = 'Si'
        else:
            # si la condicion se cumple añade el valor 'Si' a la columna Justificacion requerida
            linea['justificacion recibida'] = 'No'
        linea['justificacion recibida'] = 'No'
        # volcamos la informacion obtenida en el escritor 'fichero a crear'
        escritor.writerow(linea)
