# Heladería tiene clientes
# los clientes quieren ver el menú, tomar un helado, tomar una bebida y pedir la cuenta
# dic=c,v for c,v in dic.items():
# lista = [] for i in lista:
# conjunto=(), inmutable
# coding=utf-8
class IceCreamShop:
    total = 0
    listado = [0]
    sabor = ''
    drink = ''
    cantidadBebidas = 0
    cantidadHelados = 0

    def __init__(self, lista):
        self.listado = lista

    def verLista(self):
        count = 0
        while count < len(self.listado):
            print("tengo: ", self.listado[count])
            count += 1

    def helado(self):
        self.sabor = input("Elige un sabor de helado: ")
        cantidadHelado = int(input("cantidad de bolas: "))
        count = 0
        for i in self.listado:
            if self.sabor in i['nombre']:
                self.cantidadHelados = cantidadHelado
                self.total = self.total + self.listado[count]['precio'] * self.cantidadHelados
            else:
                pass
                count += 1

    def bebida(self):
        self.drink = input("que bebida desea: ")
        self.cantidadBebidas = int(input("cantidad: "))
        count = 0
        for i in self.listado:
            if self.drink in i['refresco']:
                self.total = self.total + self.listado[count]['precioBebida'] * self.cantidadBebidas

            else:
                pass
                count += 1

    def cuenta(self):
        print("Su cuenta es:")
        print("helado de sabor: ", self.sabor, ' ', self.cantidadHelados)
        print("bebida: ", self.drink, ' ', self.cantidadBebidas)
        print("total a pagar: ", self.total)
