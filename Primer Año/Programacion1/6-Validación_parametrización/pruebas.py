# try:
#     n=int("hola")
#     print("esro viende despues del int")
# except:
#     print("no puede convertit")

# validado=False
# while not validado:
#     try:
#         n1=int(input("ingrese un entero: "))
#         validado=True
#         print("es un entero")
#     except:
#         print("no es un entero")
def inputInt(msg):
    validado = False
    while not validado:
        try:
            n = int(input(msg))
            validado = True
            print("es un entero")
        except:
            print("no es un entero")
    return n


n1 = inputInt("ingrese el primer entero: ")
n2 = inputInt("ingrese el segundo entero: ")
print(n1+n2)
