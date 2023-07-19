# 2 formas de escritura

# 1. write()
# 'w' escribe de cero
with open('7-Archivos/escrti.txt', 'w') as pedorry:
    pedorry.write('cualquier gilada\n')

# 'a' agrega al fondo del archivo
with open('7-Archivos/escrti.txt', 'a') as pedorry:
    # write() escribe una string
    pedorry.write('segunda gilada')


# 2. writelines() escribe una lista
lista = ['Josefa\n', 'Antonio\n']
with open('7-Archivos/escrti.txt', 'w') as pedorry:
    pedorry.writelines(lista)