"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
import random
def generador(mayuscula=False,numeros=False,simbolos=False,miniMo=None, maxiMo=None):
    longitud=random.randint(miniMo, maxiMo)
    abece = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    carac = "#$%&"
    contra=""
    for rec in range(longitud):
        if len(contra) <= longitud:
            if mayuscula == True:
                contra=contra + random.choice(abece).upper()
            if numeros == True:
                contra = contra + random.choice(num)
            if simbolos == True:
                contra = contra + random.choice(carac)
            contra = contra + random.choice(abece)
    print(longitud)
    return contra[:longitud]

print(generador(mayuscula=True,numeros=True,simbolos=True,miniMo=8, maxiMo=16))
