
frase = "se repite una letra cualquiera"
rep = "a"


def contadorDef(letra, cadena):
    contador = 0
    for x in cadena:
        if x == letra:
            contador = contador+1
    return contador


print("cantidad de veces que repite la letra", rep,)
print(contadorDef(rep, frase))
print(contadorDef("o", "jonathan desplats"))
