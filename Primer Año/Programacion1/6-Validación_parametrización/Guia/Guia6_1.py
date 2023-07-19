def concatenar(*args, conector=" "):  # tupla
    frase = ""
    if conector != " ":
        for rec in args:
            frase += rec + conector
            tam = len(conector)
        return frase[:len(frase)-tam]
    else:
        for rec in args:
            frase += rec + " "
        return frase


print(concatenar("Ferrari", "Mercedes", "RedBull", "Alpine"))
print(concatenar("Ferrari", "Mercedes", "RedBull", "Alpine", conector="///"))
