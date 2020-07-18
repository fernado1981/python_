from personal import personal
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección>
# y su número de teléfono es <teléfono>.

class PersonalData:
    datos = {'Nombre': input("Nombre: "), 'Edad': int(input("Edad: ")), 'Dirección': input("Dirección: "),
             'teléfono': int(input("Teléfono: "))}

    dato = personal(datos)
    dato.verDatos()
