# Pasar una palabra a mayúsculas cambiando los caracteres uno por uno usando la tabla ASCII de referencia (googlear la tabla y las funciones de conversión en Python).
frase = "Quiero comer manzanas, solamente manzanas."
palabraVieja = "manzanas"
palabraNueva = "peras"

while palabraVieja in frase:
    posicionPalabraVieja = frase.find(palabraVieja)
    inicio = frase[:posicionPalabraVieja]
    final = frase[posicionPalabraVieja+len(palabraVieja):]
    frase = inicio + palabraNueva + final
print(frase)
