from Divisas import Divisas
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa y muestre su símbolo
# o un mensaje de aviso si la divisa no está en el diccionario.

class Divisa:
    divi = {"Euro": '€', "Dollar": '$', "Yen": '¥'}
    moneda = ['€', '$', '¥']
    divisa = Divisas(divi, moneda)
    divisa.verDivisas()
