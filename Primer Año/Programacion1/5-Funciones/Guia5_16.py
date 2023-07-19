#Implementa una función que determine si una cadena de texto contiene solo caracteres numéricos (es decir, si es un entero).
frase="Hoy es 29 de Junio de 1987"
frase2="2023"
def caracNum(texto):
    if texto[1] in "0123456789":
        return "la frase contiene solo numeros"
    else:
        return "la frase no contiene solo numeros"
print(caracNum(frase))
print(caracNum(frase2))