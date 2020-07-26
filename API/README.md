[Principal](../README.md)<br/>
[Api_Post](../Cheat_Sheet/API_post.md) | [Api_Get](../Cheat_Sheet/API_Get.md)  | [set_conjuntos](../Cheat_Sheet/set_conjunto.md) | [lista_array](../Cheat_Sheet/lista_Array.md) | [Selenium](../Cheat_Sheet/selenium.md) | [SeleniumII](../Selenium/README.md)

# PETICIONES HTTP:<br/>
    paquete request<br/>
    pip3 install requests<br/>

## Solicitud GET

Get de listado:<br/>
------------------
    url = 'https://jsonplaceholder.typicode.com/todos/'<br/>
    response = requests.get(url)<br/> 
    print(response.status_code)<br/>
    jsonRes = response.json()<br/>

Get por id:<br/>
--------------
    url = 'https://jsonplaceholder.typicode.com/todos/1'<br/>
    response = requests.get(url)<br/>
    print(response.status_code)<br/>
    responseJson = response.json()<br/>
    print(responseJson)<br/>
 
## Solicitud POST

Post de listado: <br/>
-------------------
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data=None) <br/>
    jsonRes = response.json()<br/>
    print(response.status_code) <br/>
    print(jsonRes) <br/>

Post filtrado por title y userId:1 <br/>
------------------------------------
    data = {'title': 'Pyton Requests', 'body': 'Requests are qwesome', 'userId': 1} <br/>
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data, stream=True) <br/>
    jsonRes = response.json() <br/>
    print(response.status_code) <br/>
    print(jsonRes['title'], jsonRes['body'], sep=' : ') <br/>
 
 
## Métodos de acceso:<br/>
deleteValue:
------------
    def deleteValue(self, item, val):
        for c, v in self.dicRes.items():
            if self.dicRes[item] == val:
                del self.dicRes[item]
                break
            else:
                print("No encontrado el valor para el item")
        print(c, v)
addValue:
----------
    def addValue(self, item, val):
        if item in self.dicRes:
            print("El ", item, " con el valor ", val, "ya existe en el diccionario")
        else:
            print("Añadimos elemento")
            self.dicRes[item] = val
Comparation:
------------
    def comparation(self):
        if self.dicRes == self.dicExpect:
            print("El resultado del dicionario con el experado son iguales")
        else:
            print("Diferentes")
showResult:
----------
    def showResult(self):
        print(self.dicRes)
