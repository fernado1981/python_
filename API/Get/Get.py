class Get:
    dicRes = {}
    dicExpect = {}
    value = ''

    #constructor para inicializar las variables necesarias
    def __init__(self, responseDic, expectedResponse):
        self.dicRes = responseDic
        self.dicExpect = expectedResponse

    #método para eleminar clave:valor del diccionario   
    def deleteValue(self, item, val):
        for c, v in self.dicRes.items():
            if self.dicRes[item] == val:
                del self.dicRes[item]
                print("Eliminado", item, "con valor :", val)
                break
            else:
                print("No encontrado el valor para el item")
        print(c, v)

    #Añadimos valores por clave:valor al diccionario    
    def addValue(self, item, val):
        print("pasas item: ", item, " valor: ", val)
        if item in self.dicRes:
            print("El ", item, " con el valor ", val, "ya existe en el diccionario")
        else:
            print("Añadimos elemento")
            self.dicRes[item] = val
    
    #comparamos el response obtenido con lo experado
    def comparation(self):
        if self.dicRes == self.dicExpect:
            print("El resultado del dicionario con el experado son iguales")
        else:
            print("Diferentes")
    
    #mostramos el resultado
    def showResult(self):
        print(self.dicRes)
