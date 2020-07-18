class InteractuarFactura:
    facturas = {}
    clave = 'null'
    valor = 'null'

    def __init__(self,factura,coste):
        self.clave = factura
        self.valor = coste
        self.facturas[self.clave] = self.valor

    def anadirOrden(self):
        print("Añadir")
        self.clave = int(input("Numero de Factura: "))
        self.valor = float(input("Coste de la factura: "))
        self.facturas[self.clave] = self.valor
        print(self.facturas)

    def pagarOrden(self):
        for c, v in self.facturas.items():
            print("Tiene las siguientes facturas pendiente", c)
        clave = int(input("cual desea pagar: "))
        del (self.facturas[clave])

    def terminar(self):
        for c, v in self.facturas.items():
            print("Tiene las siguientes facturas pendiente", c)
