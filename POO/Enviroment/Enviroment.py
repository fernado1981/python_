# empresa tiene clientes
# los clientes tiene nombre, apellidos e identificacion
# la empresa puede mostrar clientes y borrar clientes
# dic=c,v for c,v in dic.items():
# lista = [] for i in lista:
# conjunto=(), inmutable
# coding=utf-8
class Enviroment:
    my_client = [0]
    id = ''
    client = {}

    def __init__(self, ClientList):
        self.my_client = ClientList

    def ClientShow(self):
        for i in self.my_client:
            print(i)

    def DelClient(self, id):
        self.id = id
        count = 0
        while count < len(self.my_client):
            if self.my_client[count]['DNI'] == self.id:
                del (self.my_client[count])
                return self.id
            count += 1

    def AddClient(self, client):
        self.client = client
        self.my_client.append(self.client)
        return self.my_client[-1]['DNI']
