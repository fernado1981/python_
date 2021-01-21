<a name='top'></a>

[PRINCIPAL](README_PyRest.md) 

# DELETE API:

### Generar el fichero get.py:
    touch delete.py
 
### Agregar el siguiente contenido: 
    from flask import Flask, jsonify, request, make_response
    
    #object Flask is created and stored on app variable
    app = Flask(__name__)
    
    #arrya of dictionaries is created and stored in accounts variable
    accounts = [
        {'name': 'billy', 'balance': 450},
        {'name': 'Kelly', 'balance': 250}
    ]
    
    @app.route("/")
    def helloWorld():
        return "Hello World\n"
    
    #defined API point/accounts and request method get
    @app.route("/accounts", methods=['GET'])
    #function getAccounts, transform account in json and return it
    def getAccounts():
        return jsonify(accounts)
    
    @app.route("/account/<id>", methods=['GET'])
    def getAccount(id):
        id = int(id) - 1
        return jsonify(accounts[id])
    
    @app.route("/addaccount", methods=['POST'])
    def addAccount():
        name = request.json['name']
        balance = request.json['balance']
        data = {'name': name, 'balance': balance}
        accounts.append(data)
    
        return jsonify(data)
    
    @app.route("/delaccountname/<name>", methods=['DELETE'])
    def deleteAccountname(name):
        for i in accounts:
            if i['name'] == name:
                accounts.remove(i)
        return jsonify(accounts)
    
    @app.route("/delaccountid/<id>", methods=['DELETE'])
    def deleteAccountid(id):
        id = int(id) - 1
        print(id)
        for i in range(len(accounts)):
            if i == id:
                accounts.pop(i)
        return jsonify(accounts[id])
    
    
    ##APP.run the server
    if __name__ == "__main__":
        app.run(port=8084)
        
### Levantar el servidor flask:
    python3 get.py
    
### Eliminar por nombre:
by_id:    

    MacBook-Pro:python$ curl -X DELETE http://127.0.0.1:8084/delaccountid/<id>
    MacBook-Pro:python$ curl -X DELETE http://127.0.0.1:8084/delaccountid/1
    
by_name
    
    MacBook-Pro:python$ curl -X DELETE http://127.0.0.1:8084/delaccountname/<name>
    MacBook-Pro:python$ curl -X DELETE http://127.0.0.1:8084/delaccountname/Kelly


[Subir](#top)