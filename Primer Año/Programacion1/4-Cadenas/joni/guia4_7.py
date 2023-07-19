# Buscar una palabra y reemplazarla por otra todas las veces que aparezca. Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.' Sin usar replace.
frase = "Quiero comer manzanas, solamente manzanas. manzanas."
palabraB = "manzanas"
palabraR = "peras"
nuevaF = ""

buscar = frase.find(palabraB)

while buscar != -1:
    # en la primera vuelta del while me dice
    # nuevaF:Vacio / frase[:buscar]:Quiero comer / palabraR:peras
    nuevaF = nuevaF + frase[:buscar] + palabraR
    # armo de nuevo la palabra frase y me va a quedar: , solamente manzanas. manzanas
    frase = frase[buscar + len(palabraB):]
    # en esta misma vuelta busco la palabra nuevamente

    buscar = frase.find(palabraB)

print(nuevaF)
