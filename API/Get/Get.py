import requests


class Get:
    dicExpect = {}
    url = ''
    response = ''

    # constructor para inicializar las variables necesarias
    def __init__(self, Url, expectedResponse):
        self.url = Url
        self.dicExpect = expectedResponse

    def obtGet(self):
        # hacemos la peticion get pasandole la url
        response = requests.get(self.url)
        # imprimimos el status
        print(response.status_code)
        # parseamos a json la response
        self.responseJson = response.json()

    # método para eleminar clave:valor del diccionario
    def deleteValue(self, item, val):
        for c, v in self.responseJson.items():
            if self.responseJson[item] == val:
                del self.responseJson[item]
                print("Eliminado", item, "con valor :", val)
                break
            else:
                print("No encontrado el valor para el item")
            print(c, v)

    # Añadimos valores por clave:valor al diccionario
    def addValue(self, item, val):
        print("pasas item: ", item, " valor: ", val)
        if item in self.responseJson:
            print("El ", item, " con el valor ", val, "ya existe en el diccionario")
        else:
            print("Añadimos elemento")
            self.responseJson[item] = val

    # comparamos el response obtenido con lo experado
    def comparation(self):
        print(self.responseJson)
        if self.responseJson == self.dicExpect:
            print("El resultado del dicionario con el experado son iguales")
            self.responseJson['result'] = True
        else:
            print("Diferentes")
            self.responseJson['result'] = False

    # mostramos el resultado
    def showResult(self):
        print(self.responseJson)
