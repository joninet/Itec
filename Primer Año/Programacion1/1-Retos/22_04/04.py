# Tablero de ajedrez: Solicitar al usuario número de fila y de columna y devolver el color de la casilla (blanca o negra). Si el usuario ingresa un número que no corresponde a una casilla mostrar afuera.
fila = 0
while fila >= 0:
    fila = int(input("Ingrese el numero de la Fila: "))
    colum = int(input("Ingrese el numero de la columna: "))
    resultado = (fila+colum)/2
    if resultado == int(resultado):
        print("El casillero es blanco")
    else:
        print("el casillero es Negro")
