

```python
###dos listas generamos una lista de dos dimensiones y lo recorremos
#####################################################################
listA = ["fernando","manrique","villanueva"]
listB = ["Diego", "Manrique", "Villanueva"]
Lista =  [listA] + [listB]
print(Lista)

aux=1;n=0;j=0;z=0
while n < len(Lista):
    while j < len(Lista):
        while z < len(Lista):
            print(Lista[z][n],' ',Lista[z][aux],' ',Lista[z][aux+1])
            z +=1
        j +=1
    n +=1
```

    [['fernando', 'manrique', 'villanueva'], ['Diego', 'Manrique', 'Villanueva']]
    fernando   manrique   villanueva
    Diego   Manrique   Villanueva



```python
###dos conjuntos en una lista y la lista a diccionario
#######################################################
conjuntoA={"fernando","manrique","villanueva"}
conjuntoB={"Diego","Manrique","Villanueva"}
lista = [conjuntoA] + [conjuntoB]
print("->los dos conjunto en una lista: ")
print(lista)

dic ={}
count=0
for n in lista:
    for i in n:
        dic[count]= i
        count +=1

print("->transformo el contenido a un diccionariuo clave valor: ")
print(dic)
      
print("->obtengo el valor de la clave 0: ")
print(dic[0])  

print("->imprimo el dicionario por clave valor: ")
for c,v in dic.items():
          print(c,v)
```

    ->los dos conjunto en una lista: 
    [{'manrique', 'villanueva', 'fernando'}, {'Manrique', 'Villanueva', 'Diego'}]
    {'manrique', 'villanueva', 'fernando'}
    {'Manrique', 'Villanueva', 'Diego'}
    ->transformo el contenido a un diccionariuo clave valor: 
    {0: 'manrique', 1: 'villanueva', 2: 'fernando', 3: 'Manrique', 4: 'Villanueva', 5: 'Diego'}
    ->obtengo el valor de la clave 0: 
    manrique
    ->imprimo el dicionario por clave valor: 
    0 manrique
    1 villanueva
    2 fernando
    3 Manrique
    4 Villanueva
    5 Diego



```python
#dos dicionarios en un array y recorremos
news={"periodico":"pepe","url" : "pepito"}
news1={"periodico":"pepe","url" : "pepitin"}

NEWS=[news] + [news1]

#muestra todo el contenido de la lista
for n in  NEWS:
   print(n)  


#muestra el contenido de la lista con un contador de esa manera se puede controlar
count=0
for n in NEWS:
    print(" periodico :",NEWS[count]['periodico'],'url: ',NEWS[count]['url'])
    count +=1
```

    {'periodico': 'pepe', 'url': 'pepito'}
    {'periodico': 'pepe', 'url': 'pepitin'}
     periodico : pepe url:  pepito
     periodico : pepe url:  pepitin



```python
##programa pedido en una heladeria, se pueden pedir helados de diferentes sabor y n bolas
##ademas se puede pedir bebida con n consumiciones
##al final da la cuenta al cliente, reflejando lo tomado cantidad y precio
#########################################################################################
##clase pedido
class pedido(): 
    
    total=0; listado=[0]; sabor=''; drink=''; cantidadBebidas=0; cantidadHelados=0

    def __init__(self,lista):
        self.listado=lista


    def verLista(self):
        count=0
        while count < len(self.listado):
            print("tengo: ",self.listado[count])
            count +=1

    def helado(self):
        print("Elige un sabor de helado")
        sabor=input()
        print("cantidad de bolas")
        cantidadHelado=int(input())
        self.sabor=sabor
        count=0
        for i in self.listado:
            if(self.sabor in i['nombre']):
                self.cantidadHelados=cantidadHelado
                self.total=self.total+self.listado[count]['precio']*self.cantidadHelados
            else:
                pass
                count +=1


    def bebida(self):
        print("que bebida desea")
        bebida=input()
        print("cantidad")
        cantidadBebida=int(input())
        self.drink=bebida
        self.cantidadBebidas=cantidadBebida
        count=0
        for i in self.listado:
            if(self.drink in i['refresco']):
                self.total=self.total+self.listado[count]['precioBebida']*self.cantidadBebidas
                
            else:
                pass
                count +=1
 
        
    def cuenta(self):
        print("Su cuenta es:")
        print("helado de sabor: ",self.sabor,' ',self.cantidadHelados)
        print("bebida: ",self.drink,' ',self.cantidadBebidas)
        print("total a pagar: ",self.total)
    

#clase ejecutora o principal
class ejecutor():

    helados={"nombre":"Mango","precio": 1.50,"refresco":"cola","precioBebida" : 2.50}
    heladosA={"nombre":"Fresa","precio": 3.50,"refresco":"piña","precioBebida" : 3.50}
    heladosB={"nombre":"Nata","precio": 2.50,"refresco":"fanta","precioBebida" : 2.50}

    lista=[helados] + [heladosA] +[heladosB]

    cliente = pedido(lista)
    cliente.verLista()
    cliente.helado()
    cliente.bebida()
    cliente.cuenta()
```

    tengo:  {'nombre': 'Mango', 'precio': 1.5, 'refresco': 'cola', 'precioBebida': 2.5}
    tengo:  {'nombre': 'Fresa', 'precio': 3.5, 'refresco': 'piña', 'precioBebida': 3.5}
    tengo:  {'nombre': 'Nata', 'precio': 2.5, 'refresco': 'fanta', 'precioBebida': 2.5}
    Elige un sabor de helado
    Mango
    cantidad de bolas
    4
    que bebida desea
    piña
    cantidad
    3
    Su cuenta es:
    helado de sabor:  Mango   4
    bebida:  piña   3
    total a pagar:  16.5



```python
listasA={"nombre": "Fernando", "Edad": 23}
listasB={"nombre": "Manuel", "Edad": 28}

totalListas= [listasA]+[listasB]

print(totalListas)

#mostrar solo los diccionarios del array[{1}{2}]
for i in totalListas:
    print("imprimimos los diccionarios",i)
    
#mostramos cada clave valor de los diccionarios del array [{k:v}{k:v}]
#for
count=0
for i in totalListas:
    if(count == 0):
        print("for nombre: ",totalListas[count]['nombre'],' Edad: ',totalListas[count]['Edad'])
    count +=1

#while
count=0
while count < len(totalListas):
    if(count == 1):
        print("con while nombre: ",totalListas[count]['nombre'],' Edad: ',totalListas[count]['Edad'])
    count+=1
    
#mostrar dicionario clave:valor {k:v}
for c,v in listasA.items():
    print("for por clave: ",c," valor: ",v)
```

    [{'nombre': 'Fernando', 'Edad': 23}, {'nombre': 'Manuel', 'Edad': 28}]
    imprimimos los diccionarios {'nombre': 'Fernando', 'Edad': 23}
    imprimimos los diccionarios {'nombre': 'Manuel', 'Edad': 28}
    for nombre:  Fernando  Edad:  23
    con while nombre:  Manuel  Edad:  28
    for por clave:  nombre  valor:  Fernando
    for por clave:  Edad  valor:  23

