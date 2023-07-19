for i in range(5):
    print(i)
    if i == 2:
        print("este es un dos!!!!!")

""" 
valorInicial = 3
valorFinal = 7
for varRecorrido in range(valorInicial, valorFinal):
    print(varRecorrido) """


for i in range(5):
    print(i)

n = 0  # inicializar
while n < 5:
    print(n)
    n = n + 1  # contador

name = ""
while name != 'Paul':
    name = input('Name: ')


hayAsistentes = "si"
total = 0 # inicialización
while hayAsistentes == "si":
    nombre = input('Nombre: ')
    costo = int(input('Aporte voluntario: '))
    total = total + costo # acumulador
    hayAsistentes = input('Hay mas asistentes? (si/no): ')

print('Juntamos', total, "pesos")