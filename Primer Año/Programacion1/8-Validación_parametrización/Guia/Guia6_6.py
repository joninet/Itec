from input_int import inputInt

edad = inputInt('Ingrese su edad: ')
print(f'Tenés {edad} años') # f-string

n = inputInt('Ingrese un entero entre 3 y 7: ', 3, 7)
m = inputInt('Cualquier número entero: ')
maxito = inputInt('ingrese un entero menor a 1000: ', maxi=999)
minito = inputInt('ingrese un entero mayor a mil: ', 1001)

print(n, m, maxito, minito)
