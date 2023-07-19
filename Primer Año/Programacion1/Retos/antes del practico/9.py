# Verifique si para cada paréntesis abierto en una cadena de texto, hay un paréntesis cerrado (y solo uno) correspondiente. Además deben estar correctamente emparejados.
frase = "hola (hola como estas (hola de nuevo) (jonihola)"
lista = []
lista.append("-")
contador = 0
for x in range(len(frase)):
    letra=frase[x]
    if letra == "(":
        lista.append(letra)
    elif letra == (")"):
        lista.append(letra)
lista.append("-")
print(lista)
for rec in range(len(lista)-1):
    if lista[rec-1] != "(" and lista[rec] == "(" and lista[rec+1] == ")" and lista[rec+2] != ")":
        contador += 1
print(contador)
    
