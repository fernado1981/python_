class personal:
    datos = {}

    def __init__(self, data):
        self.datos = data

    def verDatos(self):
        print(self.datos['Nombre'], ' tiene ', self.datos['Edad'], ' vive en ', self.datos['Dirección'],
              ' con telefono ',
              self.datos['teléfono'])
