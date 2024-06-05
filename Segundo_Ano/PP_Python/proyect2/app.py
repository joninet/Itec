#nativos de python

#frameworks
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

listadoNombre=['joni', 'ana', 'jorge']
listadoPersonas = [
    dict(
        name = dict(
            first = "Jonathan",
            last = "Desplats"
        ),
        location = dict(
            city="Rio Cuarto"
        ),
        email = "joninet@msn.com"
    ),
    dict(
        name = dict(
            first = "Jorge",
            last = "Brognoni"
        ),
        location = dict(
            city="Merlo"
        ),
        email = "jorge@oul.com"
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
    listado = listadoPersonas
    return render_template (
        'personas.html',
        listado = listado
    )

@app.route('/personasAdd', methods=['POST', 'GET'])
def addPersonas():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        ciudad = request.form['ciudad']
        persona = dict(
            name = dict(
                first = nombre,
                last = apellido
            ),
            location = dict(
                city= ciudad
            ),
            email = email
        ),
        listadoPersonas.append(persona[0])
        print(listadoPersonas)
    return render_template (
        'add_personas.html',
    )

