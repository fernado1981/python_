import numpy as np


class Votar:
    name = ''
    years = 0
    votante = {}
    my_arr = []
    math_arr = []
    math_arr_aux = []
    aux = 1

    def __init__(self, nombre, edad):
        self.name = nombre
        self.years = edad
        self.votante['Nombre'] = self.name
        self.votante['Edad'] = self.years

    def couldVote(self):
        if self.votante['Edad'] >= 18:
            self.votante['Vota'] = True
        else:
            self.votante['Vota'] = False

        self.my_arr.append(self.votante)

    def seeVote(self):
        for i in range(len(self.my_arr)):
            if self.my_arr[i]['Vota']:
                print(self.my_arr[i]['Nombre'], '', self.my_arr[i]['Edad'], 'Vota')
            else:
                print(self.my_arr[i]['Nombre'], '', self.my_arr[i]['Edad'], 'No vota')

    def suma(self, x):
        self.math_arr = x
        print(self.math_arr, ' La suma es: ', sum(self.math_arr))

    def multiplica(self):
        self.math_arr_aux = self.math_arr[::-1]
        self.math_arr_aux = list(np.array(self.math_arr_aux) * np.array(self.math_arr))
        print("la multiplicacion de los elementos del array ",self.math_arr_aux)

        #bucle para recorrer una lista
        for i in range(len(self.math_arr_aux)):
            self.aux = self.aux * self.math_arr_aux[i]
        print("es :", self.aux)