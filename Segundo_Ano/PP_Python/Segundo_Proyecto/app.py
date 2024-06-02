from flask import Flask, render_template

app = Flask(__name__)

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