#permite iterar sobre un iterable y obtener el índice y el elemento correspondiente en cada iteración.
#La sintaxis de la función enumerate() es la siguiente:

enumerate(iterable, start=0)

"""Argumentos:
iterable: Un iterable, como una lista, una tupla, un rango, etc.
start: El índice inicial. El valor predeterminado es 0.
Devuelve:
Un objeto enumerate, que es un iterador que devuelve tuplas de dos elementos: el índice y el elemento correspondiente.
Ejemplos:"""

# Iterar sobre una lista
datosPumas = ["Juan", "Pedro", "María"]
for i,elemento in enumerate(datosPumas,start = 1):
    print(f"El elemento en la posición {i} es {elemento}")
#Este código imprimirá el siguiente resultado:
#El elemento en la posición 1 es Juan
#El elemento en la posición 2 es Pedro
#El elemento en la posición 3 es María

# Iterar sobre una tupla
t = ("a", "b", "c")
for i, item in enumerate(t):
    print(i, item)
# Salida:
# 0 a
# 1 b
# 2 c

# Iterar sobre un rango
for i, item in enumerate(range(10)):
    print(i, item)
# Salida:
# 0 0
# 1 1
# 2 2
# ...
# 9 9
