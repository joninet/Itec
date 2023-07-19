# Decir cuántas veces se repite una letra
# cualquiera, en un texto dado. Por recorrido.

texto = "Riquelme toma mate"
c = 0
letraBuscada = 'e'
""" for letra in texto:
    if letra == letraBuscada:
        c += 1
 """
for i in range(len(texto)):
    if texto[i] == letraBuscada:
        c += 1


print('La letra', letraBuscada, 'aparece', c, 'veces')
