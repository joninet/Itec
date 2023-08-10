def contarPais(lista,paisBuscar):
    contador=0
    resultado=""
    for x in lista:
        pais=x.split(",")[1]
        if pais == paisBuscar:
            contador += 1
    if contador > 0:
        resultado = f"El país {paisBuscar} tiene {contador} personas."
    else:
        resultado= f"No se encuentra el pais {paisBuscar}"
    return resultado