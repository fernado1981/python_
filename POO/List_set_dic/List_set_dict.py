tuple = {1, 2, 3, 4, 5, 6, 7, 8, 9}
numero = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]

print(tuple)
# conversion de set tuple a lista tuple
tuple = list(tuple)

# modificar el array tuple
count = 1
for i in range(len(tuple)):
    if tuple[i] == count:
        tuple[i] = numero[i]
    count += 1
print(tuple)

# convertir de lista tuple a set tuple
tuple = set(tuple)
print(tuple)

# eliminamos la última posicion del conjunto
tuple.pop()
print(tuple)

# eliminamos la ultima posicion de la lista
numero.pop()
print(numero)

# eliminamos la primera posicion de la lista
numero.pop(0)
print(numero)

del numero[0]
print(numero)

# añadimos a la lista
numero.append("diez")
print(numero)
numero.insert(2, "borriquito")
print(numero)