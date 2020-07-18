class creditosUNV:
    creditos = {}
    count = 0

    def __init__(self,credito):
        self.creditos=credito

    def vercreditos(self):
        for c, v in self.creditos.items():
            print(c, ' tiene ', v, ' creditos')
            self.count = self.count + v
        print("creditos total: ", self.count)