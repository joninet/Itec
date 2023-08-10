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
def fechaNacimiento(lista,letraIni):
    listaFechas=[]
    for x in lista:
        contador=0
        inicialLista=x.split(",")[0][0]
        fecha=x.split(",")[2]
        if letraIni == inicialLista:
            listaFechas.append(fecha)
    return listaFechas