# Diccionarios:

Fernando = {"Nombre": "Fernando", "Apellidos": "Manrique", "Edad": 39}<br/>
Diego = {"Nombre": "Diego", "Apellidos": "Manrique", "Edad": 27}<br/>
alumnos = {'Fernando': Fernando, 'Diego': Diego}<br/>

print(alumnos.keys())<br/>
print(alumnos.values())<br/>
print(alumnos['Fernando'].get("Nombre"))<br/>
print(alumnos['Fernando']['Nombre'])<br/>
alumnos['Fernando'].pop('Edad')<br/>
alumnos['Fernando']['Rango'] = 'Faraón'<br/>
print("tengo: ", alumnos)<br/>

for c, v in alumnos.items():<br/>
    if c == "Diego":<br/>
        for i in v:<br/>
            print(i, ':', v[i])<br/>
