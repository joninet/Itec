from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>hola mundo</h1><a href='/acerca_de'>acerca de<a>"

@app.route('/acerca_de')
def about():
    return "<h3>acerca de...</h3><a href='/'>volver<a>"

