class Cliente:
    clientes = []
    datosCliente = {}
    preferente = True
    DNI = ''

    def __init__(self):
        self.DNI = input("DNI: ")
        self.datosCliente['Nombre'] = input("Nombre: ")
        self.datosCliente['Direccion'] = input("Direccion: ")
        self.datosCliente['telefono'] = int(input("telefono: "))
        self.datosCliente['e-Mail'] = input("correo: ")
        self.datosCliente['preferente'] = input("True/False preferente: ")
        self.clientes.append({self.DNI: {"Nombre": self.datosCliente['Nombre'],
                                    "Dirección": self.datosCliente['Direccion'],
                                    "Telefono": self.datosCliente['telefono'],
                                    "e-Mail": self.datosCliente['e-Mail'],
                                    "Preferente": self.datosCliente['preferente'],
                                    }
                              })
        print("Cliente Añadido exitosamente")

    def AnadirCliente(self):
        self.DNI = input("DNI: ")
        self.datosCliente['Nombre'] = input("Nombre: ")
        self.datosCliente['Direccion'] = input("Direccion: ")
        self.datosCliente['telefono'] = int(input("telefono: "))
        self.datosCliente['e-Mail'] = input("correo: ")
        self.datosCliente['preferente'] = input("True/False preferente: ")
        self.clientes.append({self.DNI: {"Nombre": self.datosCliente['Nombre'],
                                         "Dirección": self.datosCliente['Direccion'],
                                         "Telefono": self.datosCliente['telefono'],
                                         "e-Mail": self.datosCliente['e-Mail'],
                                         "Preferente": self.datosCliente['preferente'],
                                         }
                              })
        print("Cliente Añadido exitosamente")

    def delCliente(self, dni):
        self.DNI = dni
        for i in range(len(self.clientes)):
            if self.DNI in self.clientes[i]:
                self.clientes.pop(i)
                print("Cliente eliminado")
                break
            else:
                pass

    def showClienteByDni(self, dni):
        self.DNI = dni
        for i in range(len(self.clientes)):
            if self.DNI in self.clientes[i]:
                print(self.clientes[i])
            else:
                pass

    def showClientList(self):
        print(self.clientes)

    def showPrefeClient(self):
        for i in range(len(self.clientes)):
            for c, v in self.clientes[i].items():
                for cl, va in v.items():
                    if cl == 'Preferente':
                        if va == 'True':
                            print("clientes :", c, v)
                        else:
                            pass
                    else:
                        pass

    def exit(self):
        print("Bye")
