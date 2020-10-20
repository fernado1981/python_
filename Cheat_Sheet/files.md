<a name="top"></a>

[Api_Post](Cheat_Sheet/READMEPOST.md) | [Api_Get](Cheat_Sheet/READMEGET.md)  | [Tuple_Set](Cheat_Sheet/READMETupleSet.md) | [lista_array](Cheat_Sheet/READMELIST.md) | [Diccionario](Cheat_Sheet/READMEDIC.md) | [Lectura y escritura de ficheros](Cheat_Sheet/files.md)


[Selenium](Selenium/README.md)


# funccion "open" integrada en python para la creación de objetos de tipo (file.txt ...) y obtener datos de un fichero.
Modos:
------
	Lectura 'r', 
	Escritura (new line)'w', 
	Add line 'a'

### podemos ver en que modo se encuentra un fichero con la siguiente sentencia:
	[file].mode()

### cerrar un fichero tras ser abierto:
	[file].close()

### con sentencia with, abrimos el fichero en el modo deseado y ejecutamos la sentencia al final de la misma el fichero se cerrará automaticamente, evitando así tener que cerralo.

### READ:
[File].read(), método que devuleve un string del contenido del fichero:
-----------------------------------------------------------------------
	with open("READMEDIC.md",'r') as file1:
  		file_lectura=file.read()
  		print(file_lectura)


[File].readlines(), método que devuelve una lista por cada linea sinedo la primera linea la posicion[0] y así sucesivamente:
----------------------------------------------------------------------------------------------------------------------------
	with open("READMEDIC.md",'r') as file1:
  		file_lectura=file.readlines()
  		print(file_lectura)


[file].readlines(), impirmiendo linea a linea:
----------------------------------------------
	with open("READMEDIC.md",'r') as file1:
  		for line in file1:
    		print(line)

### WRITE:
[file].write(), método para escribir:
-------------------------------------
	with open("READMEDIC.md",'w') as file1:
  		file1.weite("esto es una prueba")

[file].wirte(), desde una lista:
--------------------------------
	lines=['fernando\n','manrique\n','Deportes\n']
	with open("READMEDIC.md",'w') as file1:
  		for line in lines:
   			file1.write(line)

### copiar un file:
-------------------
	with open("READMEDIC.md",'r') as readfile:
		with open("READMEDIC.md",'w') as writefile:
			for line in readfile:
		   		writefile.write(line)
				
### Pandas DataFrames:

> References: <https://pandas.pydata.org/pandas-docs/stable/reference/frame.html>

Importar pandas:
----------------
	import pandas
construir un DataFrame desde un diccionario:
--------------------------------------------
	d = {'col1': [1, 2], 'col2': [3, 4]}
	df = pd.DataFrame(data=d)
	df
	
	Salida:
	
	    col1  col2
	0     1     3
	1     2     4

lectura de un csv:
------------------
	csv_path =[path_file.csv]
	df = pandas.read_csv(csv_path)

Imprimir las cinco primeras filas:
----------------------------------
	csv_path =[path_file.csv]
	df = pandas.read_csv(csv_path)
	df.head()



[Subir](#top)
