<a name='top'></a>
[Principal](../README.md)<br/>

[GET](README_GetApi.md) | [POST](README_PostApi.md) | [DELETE](README_DeleteApi.md)


# Instalar PyRest

###  Crear entorno virtual:
    python3 -m venv /path/to/new/virtual/environment

### crear directorio donde desplegar PyRest:
    mkdir [nombre del directorio PyRest]

### Instalar dependencia flask:
    pip3 install flask
    pip3 install requests

### Flask variables de entorno:
**Instalar la librería que nos ayudará a mantener nuestras variables de entorno configuradas en un archivo llamado .flaskenv**
    
    pip3 install python-dotenv
    
### creacion del fichero .flaskenv:
    touch .flaskenv
    
    FLASK_ENV=development
    FLASK_DEBUG=1
    FLASK_APP=blog.py
    
* FLASK_ENV=development Activa el modo desarrollo de nuestra aplicación para que esta detecte cambios en nuestras vistas, modelos y rutas de nuestra app sin necesidad de estar deteniendo y reiniciando el servidor.
* FLASK_DEBUG=1 Una vez en modo desarrollo, esta variable activa el modo debug de flask, que nos permite ver nuestros errores mientras estamos desarrollando
* FLASK_APP=blog.py Variable de entorno que nos permite usar flask run desde la consola de nuestro entorno virtual.

### Crear fichero de prueba en este caso hello.py
    cd [path del directorio PyRest]
    touch hello.py

### Escirbir primer script Flask:
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route("/")
    def helloWorld():
        return "Hello World\n"
        
    if __name__ = "__main__":
        app.run(port=8080)
    
### Correr el script en el servidor flask:
    python3 hello.py

    MacBook-Pro-de-fernando:Pyrest fernandomanrique$ python3 hello.py
    * Serving Flask app "hello" (lazy loading)
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 
### Acceder por web browser al servidor:
    http://127.0.0.1:8080/ 

### test como postman, usando Curl
    curl http://127.0.0.1:8080 

    Salida >>> Hello World

### Descativar virtualenv:
    source nombre_entorno_virtual/bin/deactivate

[Subir](#top)

