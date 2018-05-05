from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'
@app.route('/params/')
@app.route('/params/<name>')
@app.route('/params/<name>/<last_name>')
def params(name='este es un valor por default',last_name='cualquier valor como apellido'):
    return 'El parametro es: {},{}'.format(name,last_name)

if __name__ == '__main__':
    app.run(debug = True, port=8000)