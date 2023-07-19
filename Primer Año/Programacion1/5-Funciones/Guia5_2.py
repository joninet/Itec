def remplazoPalabra(texto, buscar, remplazo):
    nuevaF = ""
    buscarPal = texto.find(buscar)
    while buscarPal != -1:
        nuevaF = nuevaF + texto[:buscarPal] + remplazo
        texto = texto[buscarPal + len(buscar):]
        buscarPal = texto.find(buscar)

    nuevaF = nuevaF + texto

    return nuevaF


frase = "Quiero comer manzanas, solamente manzanas. manzanas."
palabraB = "manzanas"
palabraR = "peras"

print(remplazoPalabra(frase, palabraB, palabraR))
