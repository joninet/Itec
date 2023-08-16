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