from app import app
from flask import render_template


@app.route('/')
def helloIndex():
    return 'Hello World from Python Flask!'


@app.route('/hello')
def hello(name=None):
    return render_template('homePage/homePage.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
