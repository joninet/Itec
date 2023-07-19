# Buscar una palabra completa en un texto y contar cuántas veces está.
frase = "Quiero comer manzanas, solamente manzanas. manzanas"
palabraB="manzanas"
buscar=frase.find(palabraB)
contador=0
while buscar != -1:
  contador = contador + 1
  buscar = frase.find(palabraB, buscar+1)
print(contador)