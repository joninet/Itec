# Encontrar todos los números en una cadena de texto y totalizarlos
texto = "5 diam orci, eget condimentum ipsum convallis quis. Sed ut 4 perspiciatis, unde omnis iste natus error sit voluptatem 300 accusantium100"
textoN = ""
# for rec in range(len(texto)):
#     letra = texto[rec]
#     if letra not in ",.":
#         textoN += letra
# textoN = textoN.split()
# # print(textoN)
# num = 0
# for x in textoN:
#     if x[0] in "0123456789":
#         num += int(x)
# print(num)
letraNum=""
contador=0
for rec in texto:
    if rec in "0123456789":
        letraNum+=rec
    elif letraNum != "":
        contador+=int(letraNum)
        letraNum=""
contador+=int(letraNum)
print(contador)
