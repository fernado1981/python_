from Enviroment import Enviroment


class EnviromentClient:
    Fernando = {"DNI": 53387004, "Nombre": "Fernando", "Apellidos": "Marique"}
    Diego = {"DNI": 53387007, "Nombre": "Diego", "Apellidos": "Marique"}

    listClient = [Fernando] + [Diego]

    client = Enviroment(listClient)
    deleteClient = client.DelClient(53387007)
    print("Eliminado: ", deleteClient)
    addClient = client.AddClient({"DNI": 53387006, "Nombre": "Sara", "Apellidos": "Manrique"})
    print("añadido:", addClient)
    client.ClientShow()
