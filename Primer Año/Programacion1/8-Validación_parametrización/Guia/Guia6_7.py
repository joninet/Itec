#input con opciones (Ejemplo: ‘Quiere ingresar datos (si/no)”?)
from input_int import inputInt

def inputChoice(opciones, pregunta='Elija una opción'):
    pregunta += ': '
    listaOpc = opciones.split('/')
    for i in range(len(listaOpc)):
        print(f'{i+1}) {listaOpc[i]}')
    op = inputInt(pregunta, 1, len(listaOpc))
    return listaOpc[op-1]

q = inputChoice('si/no/a veces')
print(q)
r = inputChoice('rojo/verde/blanco/negro', 'Elija un color')
print(r)
