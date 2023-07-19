#Crea una función que calcule la suma de los dígitos de un número entero.
def sumaDigito (numero):
    contador=0
    for x in range(len(numero)):
        num=numero[x]
        contador+=int(num)
    return contador
ingNum=input("ingresar un numero para calcular la sumda de los digitos: ")
print(sumaDigito(ingNum))