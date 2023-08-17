class Gato:
    def ponerNombre(self, nombre): # método (setter)
        self.nombre = nombre # atributo de objeto

    def obtenerNombre(self):
        return self.nombre
    
unGato = Gato() # instanciación -creación del objeto-
otroGatito = Gato()

print()
 
otroGatito.ponerNombre('Michina')
print(unGato.nombre, otroGatito.obtenerNombre())

#------------------------------------------------


class Perro():
    def __init__(self, nombre, edad): # dunder constructor
        # 1) se ejecuta automáticamente en el momento de la creación del objeto
        # 2) recibe los argumentos enviados en la clase
        self.nombre = nombre
        self.edad = edad

perrito = Perro('Bobby', 7)
print(perrito.nombre, perrito.edad)

listaPerros = []
for i in range(3):
    nn = input('Nombre: ')
    ee = int(input('Edad: '))
    p = Perro(nn, ee)
    listaPerros.append(p)

for perro in listaPerros:
    print(perro.nombre, perro.edad)

#------------------------------------------------

