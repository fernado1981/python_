# vamos a trabajar con la function "open" integrada en python para la creación de objetos de tipo (file.txt ...) y obtener datos de un fichero.
Modos:
------
lectoura 'r', 
escritura (new line)'w', 
add line 'a'

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




