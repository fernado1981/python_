class listasTuplas:
    materiasA = ["lenguaje", "fisica", "quimica", "matematicas"]
    materiasB = ["Religion", "deportes", "informática", "descanso"]

    # materias=materiasA+materiasB  #todo en el mismo array

    materias = [materiasA] + [materiasB]  # dos arrays en un array
    # print(materias)

    n = 0
    z = 0
    j = 0
    while n < len(materias):
        while z < len(materias[n]):
            while j < len(materias[n]):
                print("n: ", materias[n][j], ' ', materias[n + 1][j])
                j += 1
            z += 1
        n += 1

    dicA = {"Name": "ferando", "Apellidos": "Manrique", "Edad": 39}
    dicB = {"Name": "Diego", "Apellidos": "Manrique", "Edad": 12}

    listas = []
    listas = [dicA] + [dicB]
    dicA['Color'] = "moreno"
    dicB['Color'] = "rubio"
    print(listas)
    del (dicA['Edad'])
    dicA['Edad'] = 21
    listas.append('motocicleta')
    print(listas)
    pos = listas.index('motocicleta')
    listas.pop(pos)
    print(listas)
    for i in range(len(listas)):
        if listas[i]['Edad'] >= 18:
            print("mayor: ", listas[i]['Name'], ' ', listas[i]['Edad'], ' ', listas[i]['Apellidos'])
            for c, v in listas[i].items():
                print(c, v)
        else:
            print("menor: ", listas[i]['Name'], ' ', listas[i]['Edad'], ' ', listas[i]['Apellidos'])
            for c, v in listas[i].items():
                print(c, v)

    tuplaA = {1, 2, 3, 4, 5}
    tuplaB = {6, 7, 8, 9, 10}
    c = list(tuplaA)
    pos = c.index(2)
    c.pop(pos)
    print(c)
    c[-2] = 'fernando'
    print(c)
    tuplaA = set(c)
    print(tuplaA)
    print(tuplaB)
    tupla ={}
    tupla = [tuplaA] + [tuplaB]
    print(tupla)
