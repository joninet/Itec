"""/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */"""
def param(url):
    new=url.split("?")[1].split("&")
    parametros=[]
    for x in new:
        definimos=x.split("=")[1]
        parametros.append(definimos)
    return parametros
print(param("https://retosdeprogramacion.com?year=2023&challenge=0"))




