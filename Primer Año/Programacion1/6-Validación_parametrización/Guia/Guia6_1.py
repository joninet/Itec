def concatenar(*args, conector=" "):  # tupla
    frase = ""
    for rec in args:
        frase += rec + conector
        tam = len(conector)
    return frase[:len(frase)-tam]
"""def concatenar(*args, conector=' '):
    s = ''
    for palabra in args:
        s += palabra + conector
    s = s[:-len(conector)]
    return s
"""

print(concatenar("Ferrari", "Mercedes", "RedBull", "Alpine"))
print(concatenar("Ferrari", "Mercedes", "RedBull", "Alpine", conector="///"))
