# 2. Cargar letras en una lista (while). Contar las vocales (for). Mostrar el total.
lista = []
contador = 0
entrar = "si"
while entrar == "si":
    letra = input("Ingresar letra: ")
    lista.append(letra)
    entrar = input("¿Agregar más? (si/no): ")
for letra in lista:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador = contador + 1
print("La lista de letras es:", lista)
print("El total de vocales es:", contador)
