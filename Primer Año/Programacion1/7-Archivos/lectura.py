# 4 formas de lectura

# 1. read()
with open('7-Archivos/arc.txt') as choty:
    print(choty.tell()) # posición de lectura
    todo = choty.read() # lee todo el archivo
    # y lo guarda como una string
    print(choty.tell()) 
    choty.seek(3) # mueve el puntero de lectura
    cuatroCars = choty.read(4) # lea 4 caracteres
    print(cuatroCars)
print(todo)

# 2. readline()
with open('7-Archivos/arc.txt') as choty:
    print(choty.readline())
 

# 3. readlines()
with open('7-Archivos/arc.txt') as choty:
    lineas = choty.readlines()
    print(lineas)

# # 4. recorrido con for
# with open('7-Archivos/arc.txt') as choty:
#     for linea in choty:
#         print(linea, end='')
# #4 formas de lectura
