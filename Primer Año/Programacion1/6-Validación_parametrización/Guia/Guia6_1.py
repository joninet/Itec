def concatenar(*args, conector=" "):  # tupla
    frase = ""
    for rec in args:
        frase += rec + conector
        tam = len(conector)
    return frase[:len(frase)-tam]


print(concatenar("Ferrari", "Mercedes", "RedBull", "Alpine"))
print(concatenar("Ferrari", "Mercedes", "RedBull", "Alpine", conector="///"))
