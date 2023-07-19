#Buscar todas las palabras palíndromas en una cadena de texto y almacenarlas en una lista.
frase="Buscar todas ana las palabras, palíndromas en una oso. cadena de texto"
fraseN=""
lista=[]
for rec in range(len(frase)):
    palabra=frase[rec]
    if palabra not in (",."):
        fraseN+=palabra
fraseN=fraseN.split()
for pali in fraseN:
    reves=pali[::-1]
    if pali == reves:
        lista.append(pali)
print(lista)

