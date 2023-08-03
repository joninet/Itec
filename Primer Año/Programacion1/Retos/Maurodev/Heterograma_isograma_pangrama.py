def heterograma(frase):
    for x in frase:
        busco=frase.count(x)
        contador=0
        if busco > 1:
            contador+=1       
        if contador > 0:
            resultado=False
        else:
            resultado=True
    return resultado
print(heterograma("holaa"))
def pangrama(frase):
    abece = "abcdefghijklmnopqrstuvwxyz"
    contador=0
    for x in abece:
        busco=frase.count(x)
        if busco >= 1:
            contador+=1       
    if contador > 25:
        resultado=True
    else:
        resultado=False
    return resultado, contador
print(pangrama("benjamin pidio una bebida de kiwi y fresa. Noe, sin vergüenza, la mas exquisita champaña del menu"))



