<a name="top"></a>
[Principal](../README.md)<br/>

# FICHEROS
Funccion "open" integrada en python para la creación de objetos de tipo (file.txt ...) y obtener datos de un fichero.
- Modos:

		Lectura 'r', 
		Escritura (new line)'w', 
		Add line 'a'

**NOTA:** con sentencia with, abrimos el fichero en el modo deseado y ejecutamos la sentencia al final de la misma el fichero se cerrará automaticamente, evitando así tener que cerralo.

### Importamos las librerías necesarias:

    from csv import reader
    from csv import DictReader
    
# ARCHIVOS TXT: 
### Lectura:
- read(), lee todo el contenido
**Nota:** esta es la forma más simple de leer un archivo, la cual no es eficaz si queremos buscar o modificar valores, sin embargo es eficaz si sólo queremos mostrar el texto o compararlo con otro.

        with open('../prueba.txt', 'r') as archivo:
            contenido = archivo.read()
            print(contenido)

### readlines(), lee linea a linea generado un array por cada una de ellas:
**Nota:** Mas eficaz que read() sería con readlines la cual generara un array con los valores

        with open('../prueba.txt', 'r') as archivo:
            contenido = archivo.readlines()
            print(contenido)
            for i in contenido:
                print(i)

### Archivos csv sin cabecera:
sintax: reader('archivo, delimiter=';',quotechar='"') 
**Nota:** lee linea a linea y genera un array por cada una de ellas:

        with open('../asociacion_sin_cabecera.csv', 'r') as archivo:
            contenido = reader(archivo, delimiter=';', quotechar='"')
            for i in contenido:
                print(' '.join(i))

### Archivos csv con cabecera, en este caso nos saltamos la linea de la cabecera:
- reader('archivo, delimiter,quotechar) lee linea a linea y genera un array por cada una de ellas
- next(contenido), nos saltamos la primera linea de la variable contenido la cual contiene los datos del csv
- podemos acceder a los valores de las columnas por posición

        with open('../asociacion.csv', 'r') as archivo:
            contenido = reader(archivo, delimiter=';', quotechar='"')
            cabecera = next(contenido)
            for i in contenido:
                print(i[0],i[2],i[6])

### Objeto Dictreader(), nos permite acceder por por nombre de la columna:
    with open('../asociacionCSV.csv', 'r') as archivo:
        contenido = DictReader(archivo, delimiter=',', quotechar='"')
        for i in contenido:
            print(i['Importe'])

### Objeto Dictreader(), sin cabecera nos permite acceder por por nombre de la columna:
- fieldnames=[,,,] es un array con el que podemos crear las cabeceras del .csv

        with open('../asociacionCSV.csv', 'r') as archivo:
            contenido = DictReader(archivo, delimiter=',', quotechar='"', fieldnames=['Asociacion', 'Actividad', 'Importe'])
            for i in contenido:
                print(i['Asociacion'])


- Podemos ver en que modo se encuentra un fichero con la siguiente sentencia:
		
		[file].mode()

# WRITE CSV:
- Importamos las librerías necesarias:

		from csv import writer, DictWriter

- Generamos el contenido a escribir:
		
		matriz = [
			['fernando', 1981, 39],
			['diego', 1994, 27]
		]

		matriz_header = [
			{'Nombre': 'fernando', 'F_nacimiento': 1981, 'Edad': 39},
			{'Nombre': 'diego', 'F_nacimiento': 1994, 'Edad': 27}
		]

### sin cabeceras, writer(archivo,delimiter,quoter):
- writerows('valor'), escribe una row en el fichero

		with open('../pruebaMatrizSnHeader.csv', 'w') as archivo:
   			doc = writer(archivo, delimiter=';', quotechar='"')
  			doc.writerows(matriz)
 			doc.writerows([['pepe', 1989, 23]])

### Añadir cabecera DictWriter(archivo, delimiter,fieldnames=[]):
- cabecera=['name_header','name_header','name_header',...], para añadir las cabeceras

		cabeceras = ['Nombre', 'F_nacimiento', 'Edad']
		with open('../pruebaMatrizHeader.csv', 'w') as archivo:
    			documento = DictWriter(archivo, delimiter=';', quotechar='"', fieldnames=cabeceras)
    			documento.writeheader()
    			documento.writerows(matriz_header)

# WRITE TXT:
### sin cabeceras, writer(archivo,delimiter,quoter):
- writerows('valor'), escribe una row en el fichero

		with open('../pruebaMatrizSnHeader.txt', 'w') as archivo:
   			doc = writer(archivo, delimiter=';', quotechar='"')
  			doc.writerows(matriz)
 			doc.writerows([['pepe', 1989, 23]])

### Añadir cabecera DictWriter(archivo, delimiter,fieldnames=[]):
- cabecera=['name_header','name_header','name_header',...], para añadir las cabeceras

		cabeceras = ['Nombre', 'F_nacimiento', 'Edad']
		with open('../pruebaMatrizHeader.txt', 'w') as archivo:
    			documento = DictWriter(archivo, delimiter=';', quotechar='"', fieldnames=cabeceras)
    			documento.writeheader()
    			documento.writerows(matriz_header)

### Copiar un file:
	
	with open("READMEDIC.md",'r') as readfile:
		with open("READMEDIC.md",'w') as writefile:
			for line in readfile:
		   		writefile.write(line)

# ARCHIVOS CSV:
### Lectura de un csv:

	csv_path =[path_file.csv]
	df = pandas.read_csv(csv_path)

### Imprimir las cinco primeras filas:
		
	csv_path =[path_file.csv]
	df = pandas.read_csv(csv_path)
	df.head()
		
# PANDAS DATAFRAMES:
**References:** <https://pandas.pydata.org/pandas-docs/stable/reference/frame.html>
### Importar pandas:
	
		import pandas
	
### Construir un DataFrame desde un diccionario:
	
		d = {'col1': [1, 2], 'col2': [3, 4]}
		df = pd.DataFrame(data=d)
		df

		Salida:

		    col1  col2
		0     1     3
		1     2     4


[Subir](#top)
