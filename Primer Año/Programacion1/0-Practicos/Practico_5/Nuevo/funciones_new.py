def contar_ocurrencias_pais(lista_personas, pais_buscar):
    contador = 0
    pais_buscar=pais_buscar.capitalize()
    for persona in lista_personas:
        pais = persona.split(",")[1]
        if pais == pais_buscar:
            contador += 1
    
    if contador > 0:
        resultado = f"El país {pais_buscar} tiene {contador} personas."
    else:
        resultado = f"No se encontró el país {pais_buscar}."
    
    return resultado

def fechas_nacimiento_con_inicial(lista_personas, inicial):
    fechas_nacimiento = []
    inicial=inicial.capitalize()
    for persona in lista_personas:
        inicial_lista = persona.split(",")[0][0]
        if inicial == inicial_lista:
            fechas_nacimiento.append(persona.split(",")[2])
    
    if not fechas_nacimiento:
        resultado = f"No se encontraron nombres con la inicial {inicial}."
    else:
        resultado = f"Fechas de nacimiento con la inicial {inicial}:\n" + "\n".join(fechas_nacimiento)
    
    return resultado