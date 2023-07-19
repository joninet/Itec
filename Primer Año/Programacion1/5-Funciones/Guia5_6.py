listaLetra=["a","e","i","o","f","j","y","h","ñ","p"]
def buscarVoc(lista):
    contador=0
    for rec in listaLetra:
        if rec in "a,e,i,o,u":
            contador+=1
    return contador
print("El numero de vocales que hay en la lista es:", buscarVoc(listaLetra))