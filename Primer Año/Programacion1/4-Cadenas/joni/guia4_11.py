# Averiguar qué cantidad de letras tiene la palabra más larga y cual es.
# Contar la cantidad de palabras.
frase = "Quiero comer manzanaseeeee, solamente manzanas."
nuevafrase = ""
palabraL = ""
for letra in frase:
    if letra != "," and letra != ".":
        nuevafrase += letra
nuevafrase = nuevafrase.split()
for palabra in nuevafrase:
    if len(palabra) > len(palabraL):
        palabraL = palabra
print("la palabra mas larga es ", palabraL, "y tiene", len(palabraL), "letras")
