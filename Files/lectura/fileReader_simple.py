from csv import reader
from csv import DictReader

# archivos de texto .txt
# esta es la forma más simple de leer un archivo, la cual no es eficaz si queremos buscar o modificar valores
# read(), leetodo el contenido

# with open('../prueba.txt', 'r') as archivo:
#   contenido = archivo.read()
#   print(contenido)


# la manera mas eficar sería con readlines la cual generara un array con los valores
# readlines(), lee linea a linea generado un array por cada una de ellas

# with open('../prueba.txt', 'r') as archivo:
#   contenido = archivo.readlines()
#   print(contenido)
#   for i in contenido:
#     print(i)

# archivos csv .csv sin cabecera
# reader('archivo, delimiter,quotechar) lee linea a linea y genera un array por cada una de ellas

# with open('../asociacion_sin_cabecera.csv', 'r') as archivo:
#   contenido = reader(archivo, delimiter=';', quotechar='"')
#   for i in contenido:
#    print(' '.join(i))

# archivos csv .csv con cabecera, en este caso nos saltamos la linea de la cabecera
# reader('archivo, delimiter,quotechar) lee linea a linea y genera un array por cada una de ellas
# next(contenido), nos saltamos la primera linea de la variable contenido la cual contiene los datos del csv
# podemos acceder a los valores de las columnas por posición

# with open('../asociacion.csv', 'r') as archivo:
#   contenido = reader(archivo, delimiter=';', quotechar='"')
#   cabecera = next(contenido)
#   for i in contenido:
#    print(i[0],i[2],i[6])

# objeto Dictreader(), nos permite acceder por por nombre de la columna
with open('../asociacionCSV.csv', 'r') as archivo:
    contenido = DictReader(archivo, delimiter=',', quotechar='"')
    for i in contenido:
        print(i['Importe'])

# objeto Dictreader(), sin cabecera nos permite acceder por por nombre de la columna
# fieldnames=[,,,] es un array con el que podemos crear las cabeceras del .csv
#with open('../asociacionCSV.csv', 'r') as archivo:
 #   contenido = DictReader(archivo, delimiter=',', quotechar='"', fieldnames=['Asociacion', 'Actividad', 'Importe'])
  #  for i in contenido:
   #     print(i['Asociacion'])
