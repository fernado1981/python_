<a name="top"></a>

# APUNTES BÁSICOS:

## Diccionario:
un Diccionario es un conjunto de elementos organizados por clave : valor, se podría decir que son los conocidos tippo de datos "objetos" en javascript la forma de acceso a estos es muy similar a la de las listas

    dic={"c":"valor", "clave":"valor", ^n}

- Recorrer:

        for c,v in dic.items():
            print(c,v)

- Eliminar: del()

        del (dic[posición or 'item'])

- Eliminar: pop()

        dic.pop('clave')
        print(dic)

- Añadir:

        dic[item] = val

- Añadir con update

        valor = {"Rango": "Militar"}

        dic.update(valor)
        print(dic)

- Tomar un valor específico dentro de una lista con diccionarios:

        count=0

        while count < len(lista):
             print(lista[count]['clave'])
             count+=1

        for i in range(len(lista)):
             print(lista[i]['clave'])

- Buscar dic e iterarlo:

        matrix = [4, 5, 6, {"Nombre": "Fernando"}, [2, 3, 4, 5, 6]]
        count = 0

        while count < len(matrix):
            if type(matrix[count]) == dict:
                for c, v in matrix[count].items():
                  print("calve: ", c, ' Valor: ', v)
           count += 1

- Buscar por clave:
**If in**
 
     if clave in dic

**If dic.has_Key(clave)**

    if d.has_key('x'):
     print d['x']

## Lista:
Las listas a diferencia de los diccionarios, guardan valores, estos pueden ser de todo tipo al igual que pasa en lenguajes tipo javascript

## Recorrer Listas:
**FOR**
- Muetsra la posición
       
        for i in lista:<br/>
           print(i)           //muesta la posición
           print(lista[i])    //muetsra el valor por posición

- Muestra la posición y su valor

        for i in enumerate(lista)_:
           print(i)   //(posición,valor)(posición,valor)(posición,valor)...

- Muestra la posición

         for i in range(len(lista)):
            print(i)
            print(lista[i])     //muetsra el valor por posición

**WHILE**
- Muestra el contenido del array por posición<br/>
    
        count = 0

         while count < len(lista):
            print(lista[count])
            count += 1

- Eliminar: del () / pop()

        del (lista[posición])

        pos=lista.index('elemento a buscar su posición')
        lista.pop(pos)

- Añadir: append()

        lista.append(elemento)

- Ver tamaño de una lista: len(lista)

        len(lista)

- bucle range: range(0,3)

        for i in range(0,3):
           print(i)      //0,1,2

## MÉTODOS PREDEFINIDOS:
- saber el tipo de dato: type(dato)

         dato=[1,2]
         type(dato)  //<class 'list'>

- obtener el valor de un diccionario por su clave: __getitem__(clave)

         dicA = {"Nombre": "Fer", "Edad": 39}

         def __getitem__(Nombre):
            print("tengo: ", Nombre['Nombre'])

         __getitem__(dicA)    //devuelve Fer

- insertar en lista: insert(pos,value)

         Zapatos = ["Reebok", "Adidas", "Nike"]
         value = "ascis"
         Zapatos.insert(2, value)

- insertar en lista: append(value)

         Zapatos.append(value)
         print(Zapatos)

- Eliminar: remove(value)

        Zapatos.remove('Reebok')

- Eliminar: pop(posicion)

        Zapatos.pop(0)

- Contar elementos: count(value)

         Zapatos.count("ascis")

- longuitud lista: len(lista)

      len(Zapatos)

- indice de un elemento en la lista: index(lista)

        Zapatos.index('Nike')

## :gem: class:
Al igual que en otros lenguajes de programación orientados a objetos se declara la clase padre donde se inicializan los atributos y contiene los métodos
el constructor siempre es el primero en ejecutrarse al instanciar un objeto a una clase, en el se inicializan las variables necesarias.

     class NombreClase:

- Constructor:

         def __init__(self,atributos^n):
           self.atributo = atributos

- Métodos:
Los metodos son funcionalidades muy especificas de la clase, por ejemplo añadir, eliminar, ver ...
     
    def NombreMétodo(self,atributo):
       ...

- Interactuación entre clases:
para crear un objeto de una clase que este fuera de nuestro file class, lo primnero quer debemos hacer es importar desde el fichero la clase

     from class import NameClass

una vez realizada la improtación, tendriamos acceso a la clase, instanciando un objeto de tipo la class

     NameClass = My_objtClass()

La forma de acceder a los métodos y atributos de la clase es por medio del conocido acceso de punto, lo cual una vez que pongamos nuestro objeto seguido de un punto nos mostrara los atributos y métodos a lo quer tenemos acceso

     My_objtClass

[Subir](#top)
