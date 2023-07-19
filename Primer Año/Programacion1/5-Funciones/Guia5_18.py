#Hacer una función que determine si una cadena de texto contiene todas las vocales.
frase="Hacer una función que determine si una cadena de texto contiene todas las vocales"
def encontrarVocal(texto):
    buscarA=texto.find("a")
    buscarE=texto.find("e")
    buscarI=texto.find("i")
    buscarO=texto.find("o")
    buscarU=texto.find("u")
    if buscarA != -1 and buscarE != -1 and buscarI != -1 and buscarO != -1 and buscarU != -1:
        print("En el texto estan todas Las vocales")
    else:
        print("En el texto no estan todas las vocales")
encontrarVocal(frase)





