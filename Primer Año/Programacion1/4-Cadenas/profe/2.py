# Transformar la cadena "Curso de Python" en la cadena "Curso de Programación en Python". Cortar la cadena original, agregarle el literal "Programación en" y concatenar.
s = 'Curso de Python'
posPython = s.find('Python')
comienzo = s[:posPython]
final = s[posPython:]
print(comienzo + 'programación en ' + final)
