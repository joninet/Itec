# Contar la cantidad de palabras
frase = "Quiero comer manzanas, solamente manzanas."


def contPal(texto):
    fraseN = frase.split()
    fraseN = len(fraseN)
    return fraseN


print("la cantidad de palabras que tiene la frase es: ", contPal(frase))
