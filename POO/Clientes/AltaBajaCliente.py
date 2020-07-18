from Cliente import Cliente


class AltaBajaCliente:

    client = Cliente()
    client.AnadirCliente()
    client.AnadirCliente()
    client.showClientList()
    client.showClienteByDni('53387004w')
    client.showPrefeClient()
    client.delCliente('53387004w')
    client.showClientList()
    client.exit()

