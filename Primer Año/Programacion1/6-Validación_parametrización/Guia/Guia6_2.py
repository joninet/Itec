# Escribe una función que cuente la cantidad de ocurrencias de una subcadena en una cadena de texto, permitiendo especificar si se debe realizar una búsqueda sin distinguir mayúsculas y minúsculas
frase = "Desde niña me encanta mirar la luna, por eso es que le puse de nombre Luna a mi hija"


def contarSubcadena(texto, palabra, ignorarMayusculas=True):
    contador = 0
    if ignorarMayusculas == False:
        buscarM = texto.find(palabra)
        while buscarM != -1:
            contador = contador + 1
            buscarM = texto.find(palabra, buscarM+1)
    else:
        textoMinuscula = texto.lower()
        buscar = textoMinuscula.find(palabra)
        while buscar != -1:
            contador = contador + 1
            buscar = textoMinuscula.find(palabra, buscar+1)
    return contador


print(contarSubcadena(frase, "luna", ignorarMayusculas=False))
print(contarSubcadena(frase, "luna"))

if ig
