

```python
#fibonacci
#1+1+2+3+5+8....
##################
def fibonacci(x):
    num=x
    i=2
    aux=[0,1]
    while i <= num:
        aux.append(aux[i-1]+aux[i-2])
        print(aux[i])
        i+=1

fibonacci(10)

```

    1
    2
    3
    5
    8
    13
    21
    34
    55



```python
#factorial
#5*4*3*2*1
############
def factorial(x):
    num=x
    i=num
    aux=x
    count=1
    while count <= num:
        aux=aux-1
        if(aux == 0):
            break
        else:
            i=i*aux
        #20*3 
        num-=1 
    
    return i


print("El fatorial de 5 es:",factorial(5))

```

    El fatorial de 5 es: 120



```python
##juego con array y conjunto, meter en una clase como con los diferentes metodos para añadir, eliminar y buscar
#############################
text="Lorem ipsum dolor sit amet consectetur adipiscing elit"
#split(" ") cambia los espacios por comas en un string y lo convierte a array
texto=text.split(" ")

print(texto)

palabra='sit'
count=0
while count < len(texto):
    texto[count]=texto[count].upper()
    if(palabra.upper() in texto[count]):
        texto[count]="Fernando"
        break
    count+=1

con=set(texto)
con.add('sit')
con.discard('elit')
print(con)
#conjunto no permite busqueda por index, ni por slicing
#print(con[2:])
#print(con.index[0])
#la forma de buscas es 'palabra' in conjunto y despues si quisieramos jugar con ella podriamos iterar con un while

texto=list(con)
count=0
while count < len(texto):
    if(palabra in texto[count]):
        print(count,texto[count])
        break
    count+=1


#las listas si nos permiten la busqueda avanzada por index, slicing
print("obtengo de la segunda posición en adelante:\n",texto[2:])
print("obtengo la última posicíon:\n",texto[-1])
print("invierto el array:\n",texto[::-1])
print("busco una palabra en particular:\n", texto.index('sit'))
texto.append("pepe")
print(texto)
eliminada = texto.pop(3)
print(texto)
```

    ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']
    {'Fernando', 'adipiscing', 'sit', 'IPSUM', 'LOREM', 'DOLOR', 'consectetur', 'amet'}
    2 sit
    obtengo de la segunda posición en adelante:
     ['sit', 'IPSUM', 'LOREM', 'DOLOR', 'consectetur', 'amet']
    obtengo la última posicíon:
     amet
    invierto el array:
     ['amet', 'consectetur', 'DOLOR', 'LOREM', 'IPSUM', 'sit', 'adipiscing', 'Fernando']
    busco una palabra en particular:
     2
    ['Fernando', 'adipiscing', 'sit', 'IPSUM', 'LOREM', 'DOLOR', 'consectetur', 'amet', 'pepe']
    ['Fernando', 'adipiscing', 'sit', 'LOREM', 'DOLOR', 'consectetur', 'amet', 'pepe']



```python
dicA={"Nombre":"Fernando","Edad":39,"Moreno": True}
dicB={"Nombre":"Diego","Edad":27,"Moreno": False}

dic = [dicA]+[dicB]
print(dic)

count=0
while count < len(dic):
    print("El nombre es: ",dic[count]['Nombre'],"La edad es: ",dic[count]['Edad'])
    count+=1
```

    [{'Nombre': 'Fernando', 'Edad': 39, 'Moreno': True}, {'Nombre': 'Diego', 'Edad': 27, 'Moreno': False}]
    El nombre es:  Fernando La edad es:  39
    El nombre es:  Diego La edad es:  27

