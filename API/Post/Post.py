import requests


class Post:
    dicdata = {}
    dicExpect = {}
    value = ''
    url = ''
    jsonRes = {}

    def __init__(self, Url, expectedResponse, data):
        self.url = Url
        self.dicExpect = expectedResponse
        self.dicdata = data

    def postApi(self):
        response = requests.post(self.url, self.dicdata, stream=True)
        print(response.status_code)
        self.jsonRes = response.json()

    def deleteValue(self, item):
        del self.jsonRes[item]

    def addValue(self, item, val):
        if item in self.dicdata:
            print("El ", item, " con el valor ", val, "ya existe en el diccionario")
        else:
            print("Añadimos elemento: ", item, ' ', val)
            self.dicdata[item] = val

    def comparation(self):
        for c, v in self.jsonRes.items():
            if c in self.dicExpect:
                if v in self.dicExpect[c]:
                    print("El resultado del dicionario con el experado son iguales")
                else:
                    print(False, "Son Diferentes")
                    break
            else:
                print("Diferentes")

    def showResult(self):
        print(self.dicdata)
