class alumnado:
    Fernando = {'id': 53387004, 'Apellido': 'Manrique', 'Edad': 39, 'aprobar': False, 'amonestaciones': 0}
    Fatima = {'id': 533865004, 'Apellido': 'loudiyi', 'Edad': 30, 'aprobar': False, 'amonestaciones': 0}
    Diego = {'id': 522865004, 'Apellido': 'Manrique', 'Edad': 27, 'aprobar': False, 'amonestaciones': 0}

    Alumnos = {'Fernando': Fernando, 'Fatima': Fatima, 'Diego': Diego}

    def getAlumno(self):
        return self.Alumnos

    def addalumno(self):
        Apellidos = input('Apellidos: ')
        id = int(input('DNI: '))
        Edad = int(input('Edad: '))
        aprobar = False
        amonestaciones = 0

        self.Alumnos[input('Nombre: ')] = {'id': id, 'Apellidos': Apellidos, 'Edad': Edad, 'aprobar': aprobar,
                                           'amonestaciones': amonestaciones}

    def delAlumno(self, id):
        for c, v in self.Alumnos.items():
            if v['id'] == id:
                self.Alumnos.pop(c)
                break
