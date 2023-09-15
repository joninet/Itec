from input_int import inputInt
from typing import Union, List

def inputChoice(opciones: Union[str, List[str]], pregunta='Elija una opción'):
    """
    Acota la entrada a un grupo de opciones.
    El parámetro obligatorio puede ser una string con
    las opciones separadas por slash o bien una lista
    """
    pregunta += ': '
    if type(opciones) == str:
        opciones = opciones.split('/')
    for i, opcion in enumerate(opciones, start=1):
        print(f'{i}) {opcion}')
    op = inputInt(pregunta, 1, len(opciones))
    return opciones[op-1]

if __name__ == '__main__':
    q = inputChoice('si/no/a veces')
    print(q)
    w = inputChoice(['Kelce', 'Andrews', 'Kittle'])
    print(w)
    r = inputChoice('rojo/verde/blanco/negro', 'Elija un color')
    print(r)