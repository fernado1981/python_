import csv

# abrimos el documento con encoding=latin1 para poder trabajar con tildes
with open("../asociacion.csv", encoding='latin1') as fichero_csv:
    # DictReader devuelve un objeto donde cada linea es un objeto,
    # las claves las cabeceras del csv y los valores seran los valores para cada cabecera
    lector = csv.DictReader(fichero_csv)
    asocs = {
        'importe_inicial': 0
    }
    # iteramos el objeto lector
    for linea in lector:
        print(linea['Importe'])
        subvencion = float(linea['Importe'])
        asocs['importe_inicial'] = subvencion + asocs['importe_inicial']
    print("importe total: ", asocs['importe_inicial'])
