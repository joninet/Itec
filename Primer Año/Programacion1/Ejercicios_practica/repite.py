frase = "Quiero comer manzanas, solamente manzanas.manzanas"
buscar = "manzanas"
find = frase.find(buscar)
contador = 0
for rec in frase:
    if find != -1:
        contador += 1
        find = frase.find(buscar, find+1)
print("la palabra se repite ", contador)
