class bucles:
    palabra = ''
    year = ''
    ActualYear = 0
    Born = 0
    count = 0
    tamanoTabla = 10
    tabla = 0
    passwordExcpeted = '123456'
    my_arr = []
    letra=''

    def __init__(self, Actual):
        self.ActualYear = Actual

    def pedirPalabra(self):
        self.palabra = input("Dime una palabra: ")
        count = 0
        print(len(self.palabra))
        while count < len(self.palabra):
            print(count, '=', self.palabra[count])
            count += 1

    def yearBorn(self):
        self.year = int(input("Edad: "))
        self.Born = self.ActualYear - self.year

        print("has nacido en el: ", self.Born)

        while self.count <= self.year:
            print(self.Born + self.count, ' = ', self.count)
            self.count += 1

    def impares(self):
        num = int(input("Dame numero: "))
        self.count = 1
        while self.count <= num:
            print(self.count)
            self.count += 2

    def cuentaAtras(self):
        num = int(input("Dame numero: "))
        self.count = 0
        while num >= self.count:
            print(num)
            num -= 1

    def inversion(self):
        cantidad = int(input("cantidad a invertir: "))
        interes = float(input("interes anual: "))
        anos = int(input("numero de años: "))

        self.count = 1
        while self.count <= anos:
            print("año: ", self.count, "capital obtenido: ", cantidad * interes)
            self.count += 1

    def tabla(self, x):
        self.tabla = x
        self.count = 1

        while self.count <= self.tamanoTabla:
            print(self.count * self.tabla)
            self.count += 1

    def password(self):
        while True:
            password = (input("Dime la password: "))
            if password == self.passwordExcpeted:
                print("estas dentro")
                break
            else:
                print("Ops lo sentimos vuelva a intentarlo")

    def letras(self):
        palabra = input("Dame palabra: ")

        for i in range(len(palabra)):
            self.my_arr.append(palabra[i])
        print(self.my_arr)

    def cuentaLetras(self, x):
        frase = input("dime una frase: ")
        self.letra = x
        print(frase.count(self.letra))
