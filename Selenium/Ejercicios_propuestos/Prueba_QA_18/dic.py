dic = {
    'Fernando': {'Apellidos': 'Manrique', 'Edad': 39},
    'Diego': {'Apellidos': 'Manrique', 'Edad': 27}
}

print(dic['Fernando']['Edad'])

for c, v in dic.items():
    if c == 'Fernando':
        for c, v in v.items():
            if c == 'Edad':
                print(c, v)
