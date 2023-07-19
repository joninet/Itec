#lista = ["Joni", "Fher", "Vicky", "Nacho"]
#           0        1           2                  3
#     3                4 
#for rec in range(len(lista)):
#                  4        0
#    inv=lista[len(lista) - rec - 1]
#    print(inv)


lista = ["Joni", "Fher", "Vicky", "Nacho"]
#           0        1           2                  3
#     3                4 
for rec in range(len(lista)//2):
    aux = lista[rec]
#                  4        3
    lista[rec] = lista[len(lista) - 1 - rec]
    lista[len(lista)-1-rec] = aux
print(lista)