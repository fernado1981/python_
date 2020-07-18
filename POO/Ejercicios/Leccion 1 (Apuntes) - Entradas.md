
# Entradas por teclado
Ya conocemos la función input() que lee una cadena por teclado. Su único inconveniente es que debemos transformar el valor a numérico si deseamos hacer operaciones con él:


```python
decimal = float( input("Introduce un número decimal con punto: ") )
```

    Introduce un número decimal con punto: 4.56



```python
valores = []
```


```python
print("Introduce 3 valores")
for x in range(3):
    valores.append(input("Introduce un valor >") )
```

    Introduce 3 valores
    Introduce un valor >2
    Introduce un valor >3
    Introduce un valor >4



```python
valores
```




    ['2', '3', '4']




```python
lista=["matemáticas","Ingles","fisica","quimica"]
print(lista)
count=0
while count < len(lista):
    print(lista[count])
    count +=1
'Ingles'in lista


#modifico la lista
lista[0]={"periodico": "elmundo","url":"http://www.elmundo.com"}
lista[1]={"periodico": "elpais","url":"http://www.elpais.com"}
lista[2]={"periodico": "marca","url":"http://www.marca.com"}
lista[3]={"periodico": "diariodigital","url":"http://www.diariodigital.com"}

print(lista)

n=0
print(len(lista))

while n < len(lista):
    print(lista[n]['periodico'],' ',lista[n]['url'])
    n = n+1


```

    ['matemáticas', 'Ingles', 'fisica', 'quimica']
    matemáticas
    Ingles
    fisica
    quimica
    [{'periodico': 'elmundo', 'url': 'http://www.elmundo.com'}, {'periodico': 'elpais', 'url': 'http://www.elpais.com'}, {'periodico': 'marca', 'url': 'http://www.marca.com'}, {'periodico': 'diariodigital', 'url': 'http://www.diariodigital.com'}]
    4
    elmundo   http://www.elmundo.com
    elpais   http://www.elpais.com
    marca   http://www.marca.com
    diariodigital   http://www.diariodigital.com



```python
class vehiculo():
    
    ruedas=4
    descapotable=False
    color="negro"
    plazas=4
    velocidad=0
    
    def __init__(self,descapotable,color,plazas):
        
        self.descapotable=descapotable
        self.color=color
        self.plazas=plazas
        
    def arrancar(self):
        print("tenemos el coche de color",self.color," ARRANCADO")
    
    
    def acelerar(self,velocidad):
        self.velocidad=velocidad
        return self.velocidad
    
    def frenar(self):
        self.velocidad = self.velocidad -10
        return self.velocidad
    
    def descapotar(self):
        if self.descapotable == True:
            print("con la melena al viento")
        else:
            print("dame una motosierra y te lo descapoto")
    
class ejecutor():
    coche = vehiculo(False,"amarillo",4)
    coche.arrancar()
    coche.descapotar()
    print(coche.acelerar(100))
    print(coche.frenar())
    
    cochePepino  = vehiculo(True,"rojoFerrari",2)
    cochePepino.arrancar()
    cochePepino.descapotar()
    print(cochePepino.acelerar(200))
        
        
        
        
        
```

    tenemos el coche de color amarillo  ARRANCADO
    dame una motosierra y te lo descapoto
    100
    90
    tenemos el coche de color rojoFerrari  ARRANCADO
    con la melena al viento
    200



```python
#pedimos dato
num=int(input("cuantos elementos necesitas: ")
        
#cramos las variables
n=0
materia=[]
alumno={}
#solicitamos los datos
while n <= num:
    libro=input("que estudiaste: ")
    nota=int(input("cual fue to nota: "))
    alumno={"libro" : libro,"nota" : nota}
    materia.append(alumno)
    n = n+1

#imprimimos los datos de la lista diccionario
n=0
while n < len(materia):
    print(materia[n]['libro'],' Nota',materia[n]['nota'])
    n = n+1
```

    cuantos elementos necesitas: 5
    que estudiaste: lengua
    cual fue to nota: 5
    que estudiaste: matematicas
    cual fue to nota: 8
    que estudiaste: quimica
    cual fue to nota: 6
    que estudiaste: filosofia
    cual fue to nota: 3
    que estudiaste: fisica
    cual fue to nota: 8
    que estudiaste: religion
    cual fue to nota: 7
    [{'libro': 'lengua', 'nota': 5}, {'libro': 'matematicas', 'nota': 8}, {'libro': 'quimica', 'nota': 6}, {'libro': 'filosofia', 'nota': 3}, {'libro': 'fisica', 'nota': 8}, {'libro': 'religion', 'nota': 7}]
    lengua  Nota 5
    matematicas  Nota 8
    quimica  Nota 6
    filosofia  Nota 3
    fisica  Nota 8
    religion  Nota 7



```python
loteria=[]
print("Dame valor")
for x in range(5):
    loteria.append(input())

print(loteria)
#ordenamos la lista
loteria.sort()
print(loteria)
#voltemos la lista
print(loteria[::-1])
#buscamos en la lista
'3' in loteria
#obtenemos el indice de la busqueda
pos=loteria.index('3')


```

    Dame valor
    5
    4
    3
    2
    1
    ['5', '4', '3', '2', '1']
    ['1', '2', '3', '4', '5']
    ['5', '4', '3', '2', '1']



```python
listaNum=[]
for i in range(11):
    listaNum.append(i)
    
listaNum[::-1]
```




    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]




```python
print("cuantas asignaturas has estudiado")
num=int(input())
asignatura=[]
asignaturaNota={}
for x in range(num):
    print("dime asignatura: ")
    asignature=input()
    print("dime la nota:")
    nota=int(input())
    if(nota < 5):
        print(asignature)
        asignaturaNota={"asignatura" : asignature, "NOTA" : nota}
        asignatura.append(asignaturaNota)
print(asignatura)
```

    cuantas asignaturas has estudiado
    2
    dime asignatura: 
    Lenguaje
    dime la nota:
    3
    Lenguaje
    [{'asignatura': 'Lenguaje', 'NOTA': 3}]
    dime asignatura: 
    matematicas
    dime la nota:
    2
    matematicas
    [{'asignatura': 'Lenguaje', 'NOTA': 3}, {'asignatura': 'matematicas', 'NOTA': 2}]
    [{'asignatura': 'Lenguaje', 'NOTA': 3}, {'asignatura': 'matematicas', 'NOTA': 2}]



```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

count=0
while count < len(alphabet):
    if(count%3 == 0):
        print("elimino :",count," siendo multiplo de tres")
        alphabet[count:count+1]=[]
    count += 1

print(alphabet)

```

    elimino : 0  siendo multiplo de tres
    elimino : 3  siendo multiplo de tres
    elimino : 6  siendo multiplo de tres
    elimino : 9  siendo multiplo de tres
    elimino : 12  siendo multiplo de tres
    elimino : 15  siendo multiplo de tres
    elimino : 18  siendo multiplo de tres
    ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'n', 'ñ', 'o', 'q', 'r', 's', 'u', 'v', 'w', 'y', 'z']



```python
nombre=input("Dime tu nombre:")
vocales(nombre)

def vocales(nombre):
    vocales=['a','e','i','o','u']
    vocalesNom=[]
    count=0
    while count <len(nombre):
        if nombre[count] in vocales:
            vocalesNom.append(nombre[count])
        count +=1

    for i in vocalesNom:
        print("tus vocales son: ",i)
```

    Dime tu nombre:fernando
    tus vocales son:  e
    tus vocales son:  a
    tus vocales son:  o

