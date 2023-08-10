# Extraer todas las fechas de una cadena de texto. El formato es AAAA-MM-DD
texto = "Sed condimentum 2023-10-02, diam orci, eget condimentum ipsum convallis quis. Sed ut 2022-4-5 perspiciatis, unde omnis iste natus error sit voluptatem accusantium "
textoN = ""
fechas = ""
#en este for recorro letra por letra para sacar los puntos y las comas
for rec in range(len(texto)):
    letra = texto[rec]
    if letra not in ",.":
        textoN += letra
textoN = textoN.split()#transformo la cadena a lista
#en este for recorro cada elemento de la lista
for fecha in textoN:
    lugarFecha = fecha.find("-")#busco en cada recorrido si ay un -
    if lugarFecha != -1:#si hay lo meto en una variable nueva
        fechas += fecha + " "
print(fechas)
