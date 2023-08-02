"""/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */"""
def infiltrado(cadena1,cadena2):
    letrasRepetidas=[]
    for rec in range(len(cadena2)):
        letra=cadena2[rec]
        if letra != cadena1[rec]:
            letrasRepetidas.append(letra)
    return letrasRepetidas
print(infiltrado("Me llamo.Brais Moure","Me llamo brais moure"))

