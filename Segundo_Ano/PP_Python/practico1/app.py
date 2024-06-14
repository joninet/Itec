import requests
from flask import Flask, render_template, request

app = Flask(__name__)

listadoProductos = [
    {
    'nombre': 'Harina 000',
    'categoria': 'harinas / salvados'
    },
    {
    'nombre': 'Harina Integral',
    'categoria': 'harinas / salvados'
    },
    {
    'nombre': 'Aceite Soja',
    'categoria': 'Aceites'
    },
    {
    'nombre': 'Aceite Girasol',
    'categoria': 'Aceites'
    },
]

@app.route("/")
def index():
    return render_template(
        'index.html',
        )

@app.route("/productos")
def mostrarProductos():
    return render_template('productos.html', productos = listadoProductos)


@app.route("/agregarproducto" , methods=['POST', 'GET'])
def agregarProducto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        producto = {
            'nombre': nombre,
            'categoria': categoria
        }
        listadoProductos.append(producto)
    print(listadoProductos)
    return render_template('agregar_producto.html')