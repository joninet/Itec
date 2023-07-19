# Contar la cantidad de letras(no incluir los separadores).
frase = "Quiero comer manzanas, solamente manzanas."
# print(len(frase))
contador = 0
for rec in range(len(frase)):
    letra = frase[rec]
    if letra not in " ,.":
        contador += 1
print("la cantidad de letras es", contador)
