<a name="top"></a>

[Api_Post](Cheat_Sheet/API_post.md) | [Api_Get](Cheat_Sheet/API_Get.md)  | [set_conjuntos](Cheat_Sheet/set_conjunto.md) | [lista_array](Cheat_Sheet/lista_Array.md) | [Selenium](Cheat_Sheet/selenium.md)

# :snake: python_:snake:
iré subiendo los ejercicios que voy realizando alguno siguen la estructura del enunciado, otros los hago más complejos para aumentar la destraza

Versión última de python<br/>

# Actualizar a la última version en mac:
Para cambiar la version de python instalada por defecto, a la más actualizada, debemos descargar la última version, instalarla y despúes en los ficheros .bash_profile, .zshrc  y .profile meter las siguientes lineas alias python='/usr/bin/python3' siendo alias python= [ruta donde la tengáis instalada]. despúes pasamos el source ~/.zshrc source ~/.profile source ~/.bash_profile y wola actualizado python en mac

# :memo: APUNTES BÁSICOS

## :gem: Diccionario:
un Diccionario es un conjunto de elementos organizados por clave : valor, se podría decir que son los conocidos tippo de datos "objetos" en javascript la forma de acceso a estos es muy similar a la de las listas<br/>

    dic={"c":"valor", "clave":"valor", ^n}

:dart: Recorrer:
---------
    for c,v in dic.items():
        print(c,v)

:dart: Eliminar: del()
---------------
    del (dic[posición or 'item'])

:dart: Eliminar: pop()
---------------
    dic.pop('clave')
      print(dic)

:dart: Añadir:
----------------
    dic[item] = val

:dart: Añadir con update
-------------------------
    valor = {"Rango": "Militar"}

    dic.update(valor)
    print(dic)

:dart: Tomar un valor específico dentro de una lista con diccionarios:
-----------------------------------------------------------------
    count=0

    while count < len(lista):
         print(lista[count]['clave'])
         count+=1
  
    for i in range(len(lista)):
         print(lista[i]['clave'])

:dart: Buscar dic e iterarlo:
-----------------------------
    matrix = [4, 5, 6, {"Nombre": "Fernando"}, [2, 3, 4, 5, 6]]
    count = 0

    while count < len(matrix):
        if type(matrix[count]) == dict:
            for c, v in matrix[count].items():
              print("calve: ", c, ' Valor: ', v)
       count += 1

:dart: Buscar por clave:<br/>
-----------------
>If in
 
     if clave in dic

>If dic.has_Key(clave)<br/>

    if d.has_key('x'):
     print d['x']

## :gem: Lista:
Las listas a diferencia de los diccionarios, guardan valores, estos pueden ser de todo tipo al igual que pasa en lenguajes tipo javascript<br/>

:dart: Recorrer:
---------
> FOR<br/>
> Muetsra la posición<br/>
       
    for i in lista:<br/>
       print(i)           //muesta la posición
       print(lista[i])    //muetsra el valor por posición

> Muestra la posición y su valor<br/>

    for i in enumerate(lista)_:
       print(i)   //(posición,valor)(posición,valor)(posición,valor)...

> Muestra la posición<br/>

     for i in range(len(lista)):
        print(i)
        print(lista[i])     //muetsra el valor por posición

> WHILE<br/>
> Muestra el contenido del array por posición<br/>
    
    count = 0

     while count < len(lista):
        print(lista[count])
        count += 1

:dart: Eliminar: del () / pop()
------------------------
     del (lista[posición])

    pos=lista.index('elemento a buscar su posición')
    lista.pop(pos)

:dart: Añadir: append()
----------------
    lista.append(elemento)

:dart: Ver tamaño de una lista: len(lista)
-----------------------------------
    len(lista)

:dart:bucle range: range(0,3)
-----------------------------
    for i in range(0,3):
       print(i)      //0,1,2

## MÉTODOS PREDEFINIDOS:<br/>
:dart: saber el tipo de dato: type(dato)
---------------------------------
     dato=[1,2]
     type(dato)  //<class 'list'>

:dart: obtener el valor de un diccionario por su clave: __getitem__(clave)
--------------------------------------------------------------------
     dicA = {"Nombre": "Fer", "Edad": 39}

     def __getitem__(Nombre):
        print("tengo: ", Nombre['Nombre'])

     __getitem__(dicA)    //devuelve Fer

:dart: insertar en lista: insert(pos,value)
-------------------------------------------
     Zapatos = ["Reebok", "Adidas", "Nike"]
     value = "ascis"
     Zapatos.insert(2, value)

:dart: insertar en lista: append(value)
-------------------------------------------
     Zapatos.append(value)
     print(Zapatos)

:dart: Eliminar: remove(value)
-----------------------------
     Zapatos.remove('Reebok')

:dart: Eliminar: pop(posicion)
-----------------------------
     Zapatos.pop(0)

:dart: Contar elementos: count(value)
------------------------------------
     Zapatos.count("ascis")

:dart: longuitud lista: len(lista)
------------------------------------
     len(Zapatos)

:dart: indice de un elemento en la lista: index(lista)
-------------------------------------------------
     Zapatos.index('Nike')

## :gem: class:
>Al igual que en otros lenguajes de programación orientados a objetos se declara la clase padre donde se inicializan los atributos y contiene los métodos
el constructor siempre es el primero en ejecutrarse al instanciar un objeto a una clase, en el se inicializan las variables necesarias.<br/>

     class NombreClase:

:dart: Constructor:
------------
     def __init__(self,atributos^n):
       self.atributo = atributos

:dart: Métodos:
--------
> Los metodos son funcionalidades muy especificas de la clase, por ejemplo añadir, eliminar, ver ...<br/>
     
    def NombreMétodo(self,atributo):
       ...

:dart: Interactuación entre clases:
----------------------------
> para crear un objeto de una clase que este fuera de nuestro file class, lo primnero quer debemos hacer es importar desde el fichero la clase<br/>

     from class import NameClass<br/>

> na vez realizada la improtación, tendriamos acceso a la clase, instanciando un objeto de tipo la class<br/>

     NameClass = My_objtClass()<br/>

> La forma de acceder a los métodos y atributos de la clase es por medio del conocido acceso de punto, lo cual una vez que pongamos nuestro objeto seguido de un punto nos mostrara los atributos y métodos a lo quer tenemos acceso<br/>

     My_objtClass.<br/>
     
[Subir](#top)
