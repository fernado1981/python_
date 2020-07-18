class ArticulosTienda:
    articulos = {}
    compra = True
    count = 0
    articulo = ''
    precio = 0

    def __init__(self, buy):
        self.compra = buy

    def compraArticulo(self):
        while self.compra:
            print(self.articulos)
            more = input("desea realizar compra Si/No: ")
            if more == 'Si':
                self.articulo = input("articulo: ")
                self.precio = float(input("precio: "))
                self.count = self.count + self.precio
                self.articulos[self.articulo] = self.precio
                self.compra = True
            else:
                break

    def verPrecio(self):
        for c, v in self.articulos.items():
            print("articulos", c, ' valor: ', v)
        self.compra = False
        print("Total: ", self.count)
