# :snake: python_:snake:
iré subiendo los ejercicios que voy realizando alguno siguen la estructura del enunciado, otros los hago más complejos para aumentar la destraza

Versión última de python<br/>

# Actualizar a la última version en mac:
Para cambiar la version de python instalada por defecto, a la más actualizada, debemos descargar la última version, instalarla y despúes en los ficheros .bash_profile, .zshrc  y .profile meter las siguientes lineas alias python='/usr/bin/python3' siendo alias python= [ruta donde la tengáis instalada]. despúes pasamos el source ~/.zshrc source ~/.profile source ~/.bash_profile y wola actualizado python en mac

# :memo: APUNTES BÁSICOS

## :gem: Diccionario:
un Diccionario es un conjunto de elementos organizados por clave : valor, se podría decir que son los conocidos tippo de datos "objetos" en javascript la forma de acceso a estos es muy similar a la de las listas<br/>

> dic={"c":"valor", "clave":"valor", ^n}<br/>

:dart: Recorrer:
---------
> for c,v in dic.items():<br/>
> print(c,v)<br/>

:dart: Eliminar: del()
---------------
> del (dic[posición or 'item'])<br/>

:dart: Eliminar: pop()
---------------
> dic.pop('clave')<br/>
>   print(dic)<br/>

:dart: Añadir:
----------------
> dic[item] = val<br/>

:dart: Añadir con update
-------------------------
> valor = {"Rango": "Militar"}<br/>
> dic.update(valor)<br/>
> print(dic)<br/>

:dart: Tomar un valor específico dentro de una lista con diccionarios:
-----------------------------------------------------------------
> count=0<br/>

> while count < len(lista):<br/>
>   print(lista[count]['clave'])<br/>
>   count+=1<br/>
  
> for i in range(len(lista)):<br/>
>   print(lista[i]['clave'])<br/>

:dart: Buscar dic e iterarlo:
-----------------------------
> matrix = [4, 5, 6, {"Nombre": "Fernando"}, [2, 3, 4, 5, 6]]<br/>
> count = 0<br/>

> while count < len(matrix):<br/>
>    if type(matrix[count]) == dict:<br/>
>        for c, v in matrix[count].items():<br/>
>            print("calve: ", c, ' Valor: ', v)<br/>
>    count += 1<br/>

## :gem: Lista:
Las listas a diferencia de los diccionarios, guardan valores, estos pueden ser de todo tipo al igual que pasa en lenguajes tipo javascript<br/>

:dart: Recorrer:
---------
FOR<br/>
Muetsra la posición<br/>
> for i in lista:<br/>
>   print(i)           //muesta la posición<br/>
>   print(lista[i])    //muetsra el valor por posición<br/>

Muestra la posición y su valor<br/>
> for i in enumerate(lista):<br/>
>   print(i)   //(posición,valor)(posición,valor)(posición,valor)...<br/>

Muestra la posición<br/>
> for i in range(len(lista)):<br/>
>    print(i)<br/>
>    print(lista[i])     //muetsra el valor por posición<br/>

WHILE<br/>
Muestra el contenido del array por posición<br/>
> count = 0<br/>

> while count < len(lista):<br/>
>    print(lista[count])<br/>
>    count += 1<br/>

:dart: Eliminar: del () / pop()
------------------------
> del (lista[posición])<br/>
> pos=lista.index('elemento a buscar su posición')<br/>
> lista.pop(pos)<br/>

:dart: Añadir: append()
----------------
> lista.append(elemento)<br/>

:dart: Ver tamaño de una lista: len(lista)
-----------------------------------
> len(lista)<br/>

:dart:bucle range: range(0,3)
-----------------------------
> for i in range(0,3):<br/>
>   print(i)      //0,1,2<br/>

## MÉTODOS PREDEFINIDOS:<br/>
:dart: saber el tipo de dato: type(dato)
---------------------------------
> dato=[1,2]<br/>
> type(dato)  //<class 'list'><br/>

:dart: obtener el valor de un diccionario por su clave: __getitem__(clave)
--------------------------------------------------------------------
> dicA = {"Nombre": "Fer", "Edad": 39}<br/>

> def __getitem__(Nombre):<br/>
>    print("tengo: ", Nombre['Nombre'])<br/>

> __getitem__(dicA)    //devuelve Fer<br/>

:dart: insertar en lista: insert(pos,value)
-------------------------------------------
> Zapatos = ["Reebok", "Adidas", "Nike"]
> value = "ascis"
> Zapatos.insert(2, value)

:dart: insertar en lista: append(value)
-------------------------------------------
> Zapatos.append(value)
> print(Zapatos)

:dart: Eliminar: remove(value)
-----------------------------
> Zapatos.remove('Reebok')

:dart: Eliminar: pop(posicion)
-----------------------------
> Zapatos.pop(0)

:dart: Contar elementos: count(value)
------------------------------------
> Zapatos.count("ascis")

:dart: longuitud lista: len(lista)
------------------------------------
> len(Zapatos)

:dart: indice de un elemento en la lista: index(lista)
-------------------------------------------------
> Zapatos.index('Nike')

## :gem: class:
Al igual que en otros lenguajes de programación orientados a objetos se declara la clase padre donde se inicializan los atributos y contiene los métodos
el constructor siempre es el primero en ejecutrarse al instanciar un objeto a una clase, en el se inicializan las variables necesarias.<br/>

> class NombreClase:<br/>

:dart: Constructor:
------------
> def __init__(self,atributos^n):<br/>
>   self.atributo = atributos<br/>

:dart: Métodos:
--------
Los metodos son funcionalidades muy especificas de la clase, por ejemplo añadir, eliminar, ver ...<br/>
> def NombreMétodo(self,atributo):<br/>
>   ...<br/>

:dart: Interactuación entre clases:
----------------------------
para crear un objeto de una clase que este fuera de nuestro file class, lo primnero quer debemos hacer es importar desde el fichero la clase<br/>

> from class import NameClass<br/>

una vez realizada la improtación, tendriamos acceso a la clase, instanciando un objeto de tipo la class<br/>

> NameClass = My_objtClass()<br/>

La forma de acceder a los métodos y atributos de la clase es por medio del conocido acceso de punto, lo cual una vez que pongamos nuestro objeto seguido de un punto nos mostrara los atributos y métodos a lo quer tenemos acceso<br/>

> My_objtClass.<br/>
