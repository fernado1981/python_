

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
    [{'manrique', 'fernando', 'villanueva'}, {'Manrique', 'Villanueva', 'Diego'}]
    ->transformo el contenido a un diccionariuo clave valor: 
    {0: 'manrique', 1: 'fernando', 2: 'villanueva', 3: 'Manrique', 4: 'Villanueva', 5: 'Diego'}
    ->obtengo el valor de la clave 0: 
    manrique
    ->imprimo el dicionario por clave valor: 
    0 manrique
    1 fernando
    2 villanueva
    3 Manrique
    4 Villanueva
    5 Diego



```python
news={"periodico":"pepe","url" : "pepito"}
news1={"periodico":"pepe","url" : "pepitin"}

NEWS=[news] + [news1]

#print(NEWS)

for n in NEWS:
    print("periodico :",n['periodico'],'url: ',n['url'])
```

    periodico : pepe url:  pepito
    periodico : pepe url:  pepitin



```python

```
