<a name='top'></a>

[PRINCIPAL](README_PyRest.md) 

# POST API:

### Generar el fichero get.py:
    touch post.py
 
### Agregar el siguiente contenido: 
    from flask import Flask, jsonify
    
    #object Flask is created and stored on app variable
    app = Flask(__name__)
    
    #arrya of dictionaries is created and stored in accounts variable
    accounts = [
        {'name': 'billy', 'balance': 450},
        {'name': 'Kelly', 'balance': 250}
    ]
    
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
        data = {'name': name, 'balance':balance}
        accounts.append(data)
        
        return jsonify(data)
            
    ##APP.run the server
    if __name__ == "__main__":
        app.run(port=8080)
        
### Levantar el servidor flask:
    python3 get.py
    
### Agregar nuevos datos:
    MacBook-Pro:python$ curl -X POST -H "Content-Type: application/json" -d '{"name": "Shovon", "balance": 100}' http://127.0.0.1:8083/addaccount
    {
      "balance": 100, 
      "name": "Shovon"
    }

**NOTA:** {"name": "Shovon", "balance": 100},  es el diccionario con los campos de la nueva entrada

[Subir](#top)