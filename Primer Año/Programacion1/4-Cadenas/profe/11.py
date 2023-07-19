# Averiguar qué cantidad de letras tiene la palabra más larga y cual es.
frase = "Quiero comer manzanas, solamente manzanas."
fraseLimpia = ''
# limpio de NO letras, dejo espacios
for caracter in frase:
    if caracter not in ',.':
        fraseLimpia += caracter
palabras = fraseLimpia.split()

masLarga = ''
for palabra in palabras:
    if len(palabra) > len(masLarga):
        masLarga = palabra
print('la palabra más larga es', masLarga, 'y su longitud es', len(masLarga))
