class Post:
    dicRes = {}
    dicExpect = {}
    value = ''

    def __init__(self, responseDic, expectedResponse):
        self.dicRes = responseDic
        self.dicExpect = expectedResponse

    def deleteValue(self, item, val):
        for c, v in self.dicRes.items():
            if self.dicRes[item] == val:
                del self.dicRes[item]
                print("Eliminado", item, "con valor :", val)
                break
            else:
                print("No encontrado el valor para el item")
        print(c, v)

    def addValue(self, item, val):
        print("pasas item: ", item, " valor: ", val)
        if item in self.dicRes:
            print("El ", item, " con el valor ", val, "ya existe en el diccionario")
        else:
            print("Añadimos elemento")
            self.dicRes[item] = val

    def comparation(self):
        if self.dicRes == self.dicExpect:
            print("El resultado del dicionario con el experado son iguales")
        else:
            print("Diferentes")

    def showResult(self):
        print(self.dicRes)