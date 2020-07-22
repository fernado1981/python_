# :snake: python_:snake:
iré subiendo los ejercicios que voy realizando alguno siguen la estructura del enunciado, otros los hago más complejos para aumentar la destraza

Versión última de python

# Actualizar a la última version en mac:
Para cambiar la version de python instalada por defecto, a la más actualizada, debemos descargar la última version, instalarla y despúes en los ficheros .bash_profile, .zshrc  y .profile meter las siguientes lineas alias python='/usr/bin/python3' siendo alias python= [ruta donde la tengáis instalada]. despúes pasamos el source ~/.zshrc source ~/.profile source ~/.bash_profile y wola actualizado python en mac

# :memo: APUNTES BÁSICOS

## :gem: Diccionario:
un Diccionario es un conjunto de elementos organizados por clave : valor, se podría decir que son los conocidos tippo de datos "objetos" en javascript la forma de acceso a estos es muy similar a la de las listas<br/>

> dic={"c":"valor", "clave":"valor", ^n}

:dart: Recorrer:
---------
> for c,v in dic.items():<br/>
>  print(c,v)

:dart: Eliminar: del()
---------------
> del (self.dic[posición or 'item'])

:dart: Añadir: append()
----------------
> dic[item] = val

:dart: Tomar un valor específico dentro de una lista con diccionarios:
-----------------------------------------------------------------
> count=0<br/>
> while count < len(lista):<br/>
>   print(lista[count]['clave'])<br/>
>   count+=1<br/>
  
> for i in range(len(lista)):<br/>
>   print(lista[i]['clave'])<br/>

## :gem: Lista:
Las listas a diferencia de los diccionarios, guardan valores, estos pueden ser de todo tipo al igual que pasa en lenguajes tipo javascript<br/>

:dart: Recorrer:
---------
Muetsra la posición
> for i in lista:<br/>
>   print(i)           //muesta la posición
>   print(lista[i])    //muetsra el valor por posición

Muestra la posición y su valor
> for i in enumerate(lista):
>   print(i)   //(0,x)(1,x)(2,x)

:dart: Eliminar: del () / pop()
------------------------
> del (lista[posición])<br/>
> pos=lista.index('elemento a buscar su posición')
> lista.pop(pos)

:dart: Añadir: append()
----------------
> lista.append(elemento)

:dart: Ver tamaño de una lista: len(lista)
-----------------------------------
> len(lista)

:dart:bucle range: range(0,3)
-----------------------------
> for i in range(0,3):
>   print(i)      //0,1,2

## :gem: class:
Al igual que en otros lenguajes de programación orientados a objetos se declara la clase padre donde se inicializan los atributos y contiene los métodos
el constructor siempre es el primero en ejecutrarse al instanciar un objeto a una clase, en el se inicializan las variables necesarias.<br/>

> class NombreClase:

:dart: Constructor:
------------
> def __init__(self,atributos^n):<br/>
>   self.atributo = atributos

:dart: Métodos:
--------
Los metodos son funcionalidades muy especificas de la clase, por ejemplo añadir, eliminar, ver ...<br/>
> def NombreMétodo(self,atributo):
>   ...

:dart: Interactuación entre clases:
----------------------------
para crear un objeto de una clase que este fuera de nuestro file class, lo primnero quer debemos hacer es importar desde el fichero la clase<br/>

> from class import NameClass<br/>

una vez realizada la improtación, tendriamos acceso a la clase, instanciando un objeto de tipo la class<br/>

> NameClass = My_objtClass()<br/>

La forma de acceder a los métodos y atributos de la clase es por medio del conocido acceso de punto, lo cual una vez que pongamos nuestro objeto seguido de un punto nos mostrara los atributos y métodos a lo quer tenemos acceso<br/>

> My_objtClass.<br/>
