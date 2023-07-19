#Contar la cantidad de letras (mayúsculas, minúsculas, acentuadas, eñes).
texto="Quiero comer manzanas, solamente manzanas."
def contarLetra(textoEjem):
    contador=0
    for x in range(len(textoEjem)):
        letra=textoEjem[x]
        if letra not in " .,":
            contador+=1
    print(contador)

contarLetra(texto)
