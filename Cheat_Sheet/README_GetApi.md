<a name='top'></a>

[PRINCIPAL](README_PyRest.md) 

# GET API:

### Generar el fichero get.py:
    touch get.py
 
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
    
    ##APP.run the server
    if __name__ == "__main__":
        app.run(port=8080)
        
### Levantar el servidor flask:
    python3 get.py
    
### Ver accounts en el web browser:
    http://127.0.0.1:8080/accounts
    
    Salida >>>
    [
      {
        "balance": 450, 
        "name": "billy"
      }, 
      {
        "balance": 250, 
        "name": "Kelly"
      }
    ]
   
### Ver account <id> en el browser:
    http://127.0.0.1:8080/account/1
    
    Salida >>>
      {
        "balance": 450, 
        "name": "billy"
      }
      
    http://127.0.0.1:8080/account/2
    
    Salida >>>
      {
      "balance": 250, 
      "name": "Kelly"
      }
      
### Curl get accounts:
    MacBook-Pro:Pyrest$ curl http://127.0.0.1:8080/accounts
    [
      {
        "balance": 450, 
        "name": "billy"
      }, 
      {
        "balance": 250, 
        "name": "Kelly"
      }
    ]
    
### Curl get account <id>:
    MacBook-Pro:Pyrest$ curl http://127.0.0.1:8080/account/1
    {
      "balance": 450, 
      "name": "billy"
    }
    MacBook-Pro:Pyrest$ curl http://127.0.0.1:8080/account/2
    {
      "balance": 250, 
      "name": "Kelly"
    }
    
    
    
    MacBook-Pro-de-fernando:python_ fernandomanrique$ curl -X DELETE -H "Content-Type: application/json"  http://127.0.0.1:8083/account/?name='Shavon'

[Subir](#top)