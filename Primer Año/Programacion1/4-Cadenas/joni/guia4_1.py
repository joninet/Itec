# Eliminar el plural en esta frase: “Real Madrid gana las copas.” Recorrer y quitar las eses. Sugerencia: Usar otra string.
frase = "Real Madrid gana las copas."
nuevafrase = ""
for letra in frase:
    if letra != "s":
        nuevafrase += letra
print(nuevafrase)
