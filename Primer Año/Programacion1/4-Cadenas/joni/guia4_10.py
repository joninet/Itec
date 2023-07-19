frase="quiero comer manzanas, solamenooooooote manzanas"
vocales=["a","e","i","o","u"]
cantidad=[0,0,0,0,0]
maximo=0
vocal=""
for i in range(len(vocales)):
    for letra in frase:
        if letra == vocales[i]:
            cantidad[i]+=1
for rec in range(len(vocales)):
    if cantidad[rec] >= maximo:
        maximo=cantidad[rec]
        vocal=vocales[rec]
print("en la frase la vocal", vocal, "esa la que se encuentra mas veces con un total de", maximo)

"""
for i in frase:
    if i == "a":
        cantidad[0]+=1
    elif i == "e":
        cantidad[1]+=1
    elif i == "i":
        cantidad[2]+=1
    elif i == "o":
        cantidad[3]+=1
    elif i == "u":
        cantidad[4]+=1
for rec in range(len(vocales)):
    if cantidad[rec] > maximo:
        maximo=cantidad[rec]
        vocal=vocales[rec]
print(maximo, vocal)"""