#  ¿Qué es WSGI?
WSGI (Web Server Gateway Interface) es un protocolo para que los servidores web como Nginx, lighttpd o Cherokee envíen peticiones a aplicaciones web 
desarrolladas en Python.<br />

Para poder ejecutar una aplicación WSGI lo primero que se necesita es un servidor WSGI. WSGI es tanto un protocolo como un servidor de aplicaciones.
El servidor de aplicaciones puede servir a los protocolos WSGI, FastCGI y HTTP.<br />

## Prerrequisitos:
1.- python3
2.- Flask
3.- Docker
4.- gunicorn

suponiendo que ya tengas instalado python3 y docker en tu ordenador hay que ejecutar el siguiente comando en tu terminal pip3 install gunicorn Flask

## tutorial/index.py
...    import os, sys
...    from app import app
...    #import logger
...    from flask import render_template
...    @app.route('/')
...    def helloIndex():
...        return 'Hello World from Python Flask!'
...    @app.route('/hello')
...    def hello(name=None):
...        return render_template('homePage/homePage.html')
...    if __name__ == "__main__":
...        app.run(host='0.0.0.0',port=3000)
    
## tutorial/app/__init__.py
...    from flask import Flask,jsonify, request, make_response, send_from_directory
## create the flask object
...    app = Flask(__name__,template_folder='templates')

## tutorial/app/templates/homePage/homePage.html
...    <!DOCTYPE html>
...    <html lang="en" dir="ltr">
...      <head>
...        <meta charset="utf-8">
...        <title>hello World</title>
...      </head>
...      <body>
...        <h1>hola soy una pagina en flask</h1>
...      </body>
...    </html>

## perfecto ahora podemos probar nuestra aplicación de manera local
...    python3 index.py

## ahora que nuestra aplicación esta funcionando es momento de probar de manera local Gunicorn agregando al archivo wsgi.py
tutorial/wsgi.py:
----------------
...    from index import app
...    if __name__ == "__main__":
...        app.run()

## a continuación en nuestra terminal ejecutamos:
--------------------------------------------------
...    gunicorn --bind 0.0.0.0:3000 wsgi:app


## docker
tutorial/docker-compose.yml:
---------------------------
...    version: '3.5'
...    services:
...     web_dev:
...      build: .
...      ports:
...       - "3000:3000"
...      volumes:
...       - .:/app
...      environment:
...       - ENV=development
...       - PORT=3000
...    networks:
...     default:
...      name: web_dev

tutorial/dockerfile:
-------------------
...      FROM python:3.6
...      ADD . /app
...      WORKDIR /app
...      RUN pip install -r requirements.txt
...      EXPOSE 3000
...      CMD ["gunicorn", "-b", "0.0.0.0:3000", "wsgi:app"

requirements.txt:
-----------------
...      Flask
...      gunicorn

ahora en la terminal executamos:
--------------------------------
...      docker-compose up --build
