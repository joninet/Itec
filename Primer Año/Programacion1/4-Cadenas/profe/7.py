# Buscar una palabra y reemplazarla por otra todas las veces que aparezca. Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.' Sin usar replace.
frase = "Quiero comer manzanas, solamente manzanas."
palabraVieja = "manzanas"
palabraNueva = "peras"

while palabraVieja in frase:
    posicionPalabraVieja = frase.find(palabraVieja)
    inicio = frase[:posicionPalabraVieja]
    final = frase[posicionPalabraVieja+len(palabraVieja):]
    frase = inicio + palabraNueva + final
print(frase)
