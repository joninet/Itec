# Leer dos números y luego una opción (puede ser '+' o '-'), y según la opción elegida realizar el cálculo.
n1 = int(input("ingrese su primer numero: "))
op = input("ingrese + o -: ")
n2 = int(input("ingrese su segundo numero: "))

if op == "+":
    print("Resultado de la suma", n1 + n2)
elif op == "-":
    print("Resultado de la resta", n1 - n2)
else:
    print("Ingrese un signo correcto + o -")
