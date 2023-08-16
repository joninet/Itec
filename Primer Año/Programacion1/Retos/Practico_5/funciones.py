def paisBuscar (lista,pais=" "):
    contador=0
    for x in lista:
        listaPais=x.split(",")[1]
        if pais == listaPais:
            contador+=1
    if contador == 0:
        resultado="Opción inválida"
    else:
        resultado="La cantidad de personas de ",pais,"es",contador

    return resultado

