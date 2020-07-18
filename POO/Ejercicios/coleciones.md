

```python
class periodicos:
    colores

    def __init__(self,dic):
        self.colores=dic
    
    def recorreDic(self):
        for i in self.colores:
            print(i,':',self.colores[i])
    
class ejecutor:
    colores = {'amarillo':'yellow','azul':'blue','verde':'green'}
    p = periodicos(colores)
    p.recorreDic()
```

    amarillo : yellow
    azul : blue
    verde : green



```python
periodicos = []
p={'periodico':'elmundo','url':'http://www.elmundo.com'}
periodicos.append(p)
p1={'periodico':'elpais','url':'http://www.elpais.com'}
periodicos.append(p1)
p2={'periodico':'elmarca','url':'http://www.elmarca.com'}
periodicos.append(p2)
periodicos
```




    [{'periodico': 'elmundo', 'url': 'http://www.elmundo.com'},
     {'periodico': 'elpais', 'url': 'http://www.elpais.com'},
     {'periodico': 'elmarca', 'url': 'http://www.elmarca.com'}]




```python
count=0
while count < len(periodicos):
    print("periodico: ",periodicos[count]['periodico']," url: ",periodicos[count]['url'])
    count+=1
```

    periodico:  elmundo  url:  http://www.elmundo.com
    periodico:  elpais  url:  http://www.elpais.com
    periodico:  elmarca  url:  http://www.elmarca.com



```python
#una tupla es para objetos inmutables, se comporta ()
#de manera muy parecida a las listas
tupla=(100,"Hola",[1,2,3],-50,100,50,100)
print(tupla)

#las tuplas como las listas aceptan indexacion y slicing
tupla[0]
tupla[-1]
tupla[1:]
tupla[2:]

#si queremos ver la lista de la tupla
for i in tupla:
    print(i)
    
#buscar la tupla con type
count=0
while count < len(tupla):
    #print(type(tupla[count]))
    if(type(tupla[count]) is list):
        print(tupla[count])
    count +=1

##muestra la longitud de la tupla
print("La longitud del array de la tupla es de :",len(tupla[2]))
print("la longitud de la tupla es de :",len(tupla))
#por index saber la pposición de un elemento
print("Hola esta en la posición: ",tupla.index('Hola'))
#contar cuantas veces está un elemeto
print("100 esta :",tupla.count(100)," veces")

#al ser inmutable no tiene forma de añadir elementos
```

    (100, 'Hola', [1, 2, 3], -50, 100, 50, 100)
    100
    Hola
    [1, 2, 3]
    -50
    100
    50
    100
    [1, 2, 3]
    La longitud del array de la tupla es de : 3
    la longitud de la tupla es de : 7
    Hola esta en la posición:  1
    100 esta : 3  veces



```python
#conjuntos {}
#son colecciones de elementos deshordenados unicos
conjunto = set()
conjunto ={1,2,3}
print(conjunto)

#añadir add
conjunto.add(4)
conjunto.add(0)
conjunto.add('A')
conjunto.add('Z')
conjunto.add('H')
print(conjunto)

#buscar en un grupo
grupo={"fernando","juan","mario"}
print('fernando' in grupo)
print('Juan' not in grupo)

#no puede haber elementos duplicados en el
grupo.add('fernando')
print(grupo)

#transformación de una lista en un conjunto
c=[1,2,3,4,5]
l=set(c)
print(l)
#transformación de un conjunto a una lista
l=list(c)
print(l)
```

    {1, 2, 3}
    {0, 1, 2, 3, 4, 'A', 'H', 'Z'}
    True
    True
    {'fernando', 'juan', 'mario'}
    {1, 2, 3, 4, 5}
    [1, 2, 3, 4, 5]



```python
#diccionarios clave : valor
vacio={}
type(vacio)
colores={"amarillo": "yellow", "rojo":"red","azul":"blue"}

for c,v in colores.items():
    print(c,v)
  
print("amarillo en ingles es: ",colores["amarillo"])

#ver el valor de una clave
print("azul en inges es: ",colores['azul'])

#añadir elementos al diccionario
colores['verde']="green"
print(colores)

#eliminar elementos del diccionario
del(colores['amarillo'])
print(colores)

#modificar valores del diccionario
colores['rojo']="colorado"
print(colores)

count=0
for i in colores:
    print(i,' ',colores[i])
    count +=1
```

    amarillo yellow
    rojo red
    azul blue
    amarillo en ingles es:  yellow
    azul en inges es:  blue
    {'amarillo': 'yellow', 'rojo': 'red', 'azul': 'blue', 'verde': 'green'}
    {'rojo': 'red', 'azul': 'blue', 'verde': 'green'}
    {'rojo': 'colorado', 'azul': 'blue', 'verde': 'green'}
    rojo   colorado
    azul   blue
    verde   green

