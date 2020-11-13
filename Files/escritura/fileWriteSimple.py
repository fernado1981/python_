from csv import writer, DictWriter

matriz = [
    ['fernando', 1981, 39],
    ['diego', 1994, 27]
]

matriz_header = [

    {'Nombre': 'fernando', 'F_nacimiento': 1981, 'Edad': 39},
    {'Nombre': 'diego', 'F_nacimiento': 1994, 'Edad': 27}
]

# writer(archivo,delimiter,quoter), sin cabeceras
# writerows('valor'), escribe una row en el fichero
# with open('../pruebaMatrizSnHeader.csv', 'w') as archivo:
#   doc = writer(archivo, delimiter=';', quotechar='"')
#  doc.writerows(matriz)
# doc.writerows([['pepe', 1989, 23]])

# añadir cabecera DictWriter(archivo, delimiter,fieldnames=[])
# cabecera=['name_header','name_header','name_header',...], para añadir las cabeceras
cabeceras = ['Nombre', 'F_nacimiento', 'Edad']
with open('../pruebaMatrizHeader.csv', 'w') as archivo:
    documento = DictWriter(archivo, delimiter=';', quotechar='"', fieldnames=cabeceras)
    documento.writeheader()
    documento.writerows(matriz_header)
