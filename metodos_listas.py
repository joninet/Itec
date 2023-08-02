# Añade un ítem al final de la lista:
lista.append(6)

# Vacía todos los ítems de una lista:
lista.clear()

# Une una lista a otra:
lista1.extend(lista2)

#Cuenta el número de veces que aparece un ítem:
["Hola", "mundo", "mundo"].count("Hola")

# Devuelve el índice en el que aparece un ítem (error si no aparece):
["Hola", "mundo", "mundo"].index("mundo")

# Agrega un ítem a la lista en un índice específico:
Primera posición (0):
lista.insert(0,0)
Penúltima posición (-1):
lista.insert(-1,20) 

#Extrae un ítem de la lista y lo borra:
lista = [10,20,30,40,50]
print(l.pop(0)) # extrae el primero de la lista

# Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos:
l = [20,30,30,30,40]
l.remove(30) #borra el primer 30 que encuentra

# Le da la vuelta a la lista actual:
lista.reverse()

# Ordena automáticamente los ítems de una lista por su valor de menor a mayor:
lista.sort(reverse=True)