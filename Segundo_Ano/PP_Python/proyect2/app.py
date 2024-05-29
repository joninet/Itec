#nativos de python

#frameworks
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

listadoNombre=['joni', 'ana', 'jorge']
diccionarioNombre = [
    dict(
        nombre = 'Ana',
        edad= 30,
        pais = 'Argentina',
    ),
    dict(
        nombre = 'Jorge',
        edad= 34,
        pais = 'Argentina',
    ),
    dict(
        nombre = 'Rosa',
        edad= 22,
        pais = 'Argentina',
    ),
    dict(
        nombre = 'Joni',
        edad= 36,
        pais = 'Argentina',
    ),
]

@app.route('/') # app es la instancia, route el metodo, '/' es el disparador
def index():
    return render_template(
        'index.html',
    )

@app.route('/info') # app es la instancia, route el metodo, '/' es el disparador
def informacion():
    return render_template(
        'informacion.html',
    )

@app.route('/bienvenido/<nombre>')
def bienvenido(nombre):
    return render_template('bienvenida.html', nombre=nombre)

@app.route('/personas')
def personas():
    return render_template (
        'personas.html',
    )

@app.route('/personas/add', methods=['POST', 'GET'])
def addPersonas():
    if request.method == 'POST':
        nombre = request.form['nombre'],
        apellido = request.form['apellido'],
        email = request.form['email'],
        ciudad = request.form['ciudad'],
        print(nombre)
    return render_template (
        'add_personas.html',
    )

