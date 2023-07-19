# Decir cuántas veces se repite una letra cualquiera, en un texto dado. Por recorrido.
frase = "se repite una letra cualquiera"
rep = "a"
contador = 0
for x in frase:
    if x == rep:
        contador = contador+1
print(contador)
