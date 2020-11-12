import csv

#abrimos el documento con encoding=latin1 para poder trabajar con tildes
with open("../asociacion.csv", encoding='latin1') as fichero_csv:
    #reader devuelve un objeto donde cada linea es un array
    lector = csv.reader(fichero_csv)
    # saltamos la cabecera
    next(lector, None)

    importe_total = 0
    #iteramos el objeto lector
    for linea in lector:
        print(linea)
        #hacemos la transformación a float dado que nos viene como string
        importe_str = float(linea[2])
        #calculamos la suma del importe total
        importe_total = importe_str + importe_total
    print(importe_total)


