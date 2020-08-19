a = [5, 2, 3, 1, 4]
a.sort()
print(a)

# Ordenar la lista de objetos usando un parámetro "clave"
myArray = [{"name": "Mario Peres"}, {"name": "Emilio Peres"}, {"name": "Yusaiba Peres"}]
myArray.sort(key=lambda person: person['name'])

print(myArray)
