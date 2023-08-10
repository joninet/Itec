"""/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */"""
<<<<<<< HEAD
pagina="https://retosdeprogramacion.com?year=2023&challenge=0"
buscamos=pagina.find("=")
num="0123456789"
sumamos=""
lista=[]
while buscamos != -1:
    for x in range(buscamos,len(pagina)):
        letra=pagina[x]
        if letra in num:
            sumamos=sumamos + letra
    lista.append(sumamos)
buscamos=-1
print(sumamos)
=======
def param(url):
    new=url.split("?")[1].split("&")
    parametros=[]
    for x in new:
        definimos=x.split("=")[1]
        parametros.append(definimos)
    return parametros
print(param("https://retosdeprogramacion.com?year=2023&challenge=0"))



>>>>>>> 316b22267024cf3bcc7c68bfbad23221cd4bdce2

