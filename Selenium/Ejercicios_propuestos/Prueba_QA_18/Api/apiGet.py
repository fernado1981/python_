from Selenium.Ejercicios_propuestos.Prueba_QA_18.Datos.dataApi import data


class apiGet(data):

    def __init__(self):
        self.data = data.dataApi

    def getdata(self):
        dataValue = self.getData()
        return dataValue

    def showData(self):
        print(data.dataApi)
