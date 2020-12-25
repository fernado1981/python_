## OPERADORES DE COMPARACIÓN:
Estos se utilizan para comparar dos o más valores:

        x = 2
        y = 3
        
- igual que (==):

         print(x == y)
         -> False

- deferende de (!=):

        print(x != y)
        ->True

- mayor que (>):

        print(x > y)
        -> False

- mayor o igual que (>=)

        print(x >= y)
        -> False

- menor o igual que (<=)

        print(x <= y)
        -> True
        
- menor que(<):

        print(x < y)
        -> True
        
## Operadores logicos o booleanos:
- Solo se evalúa el segundo operando si el primero es falso (a or b)

        X = True
        Y = False
        
**Nota:** Si a se evalúa a falso, entonces devuelve b, si no devuelve a

        x or Y
        -> True

- Solo se evalúa el segundo operando si el primero es verdadero (a and b)
**Nota:** Si a se evalúa a falso, entonces devuelve a, si no devuelve b

        x and Y
        -> False

- Tiene menos prioridad que otros operadores no booleanos (not a)
**Nota:** Si a se evalúa a falso, entonces devuelve True, si no devuelve False

        not x
        -> False
        
## Operadores aritméticos:
permiten realizar diferentes operaciones aritméticas como suma, resta, multiplicación, división ...

        x = 7
        y = 2
        
- suma (+):
    
        print(x+y)
        -> 9
        
- resta (-):

        print(x-y)
        -> 5
        
- producto (*):

        print(x*y)
        -> 14
        
- división (/):

        print(x/y)
        -> 3.5
        
- resto (%):

        print(x%y)
        -> 1
       
- cociente (//):

        print(x//y)
        -> 3
        
- potencia (**)

        print(x ** y)
        -> 49
        
# Operadores de asignación:
El operador de asignación se utiliza para asignar un valor a una variable (identificar un objeto con un nombre).
Como ya sabrás, este operador es el signo =. Además del operador de asignación, existen otros operadores de asignación compuestos que realizan una
operación básica sobre la variable a la que se le asigna el valor. Por ejemplo, x += 1 es lo mismo que x = x + 1.

- igual (=):

        x = 7
        print(x)
        -> 7
        
- sumar (+=):

        x += 1  # equivale a x = x+1
        print(x)
        -> 8
        
- restar (-=)

        x -= 1  # equivale a x = x-1
        print(x)
        -> 6
        
- producto (*=):

        x *= 2  # equivale a x = x*2
        print(x)
        -> 14

- división (/=):

        x /= 2  # equivale a x = x/2
        print(x)
        -> 3.5
        
- modulo (%):
 
        x %= 2  # equivale a x = x%2
        print(x)
        -> 1
        
- cociente (//):

        x //= 2  # equivale a x = x//2
        print(x)
        -> 3

- potencia (**):

        x **= 2  # equivale a x = x**2
        print(x)
        -> 49
        
# Operadores de pertenencia
Los operadores de pertenencia se utilizan para comprobar si un valor u objeto se encuentra en un objeto contenedor (list, tuple, dict, set o str).
lista = [1, 3, 2, 7, 9, 8, 6]

- in:

        print(3 in lista)
        -> True
        
- not in:

        print(3 not in lista)
        -> False
        
# Operadores dce identidad:
se utilizan para comprobar si dos variables son, o no, el mismo objeto.
        
        x = 4

- is:

        print(x is 5)
        -> False
        
        print(x is dict)
        -> False
        
        print(x is 4)
        -> True

- is not:
        print(x is not 4)
        -> False
        
        print(x is not 5)
        -> True
