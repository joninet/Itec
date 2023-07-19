# Pasar una palabra a mayúsculas cambiando los caracteres uno por uno usando la tabla ASCII de referencia (googlear la tabla y las funciones de conversión en Python).
frase = "Real Madrid gana las copas."
frase1 = ""
for x in range(len(frase)):
    frase1 = frase1 + frase[x].upper()
print(frase1)
