# Averiguar qué cantidad de letras tiene la palabra más larga.  Para ello, primero cargar cada palabra en una lista y luego obtener la solicitada. Usar dos funciones.
texto="Quiero comer manzanas, solamente manzanas."
def cargaPal(textoEjem):
    nuevaF=""
    listaPal=[]
    for x in range(len(textoEjem)):
        letra=textoEjem[x]
        if letra not in ".,":
            nuevaF+=letra
    listaPal = nuevaF.split(" ")
    return listaPal

listaBuscar=cargaPal(texto)
def contar(contarLista):
    contador = ""
    for rec in contarLista:
        if len(rec) > len(contador):
            contador = rec
    return contador
print("la palabra mas larga es: ", contar(listaBuscar))
