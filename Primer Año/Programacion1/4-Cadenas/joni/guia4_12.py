# Mostrar el valor doble del número de dos cifras (que es el único número) encontrado en la cadena. Ej.: 'Juan tiene 25 años' mostraría el número 50,
frase = "El dólar va a llegar este mes a 500 pesos casi seguro"
numeroC = ""
for i in range(len(frase)):
    numero = frase[i]
    if numero in "0123456789":
        numeroC += numero
print(int(numeroC)*2)
