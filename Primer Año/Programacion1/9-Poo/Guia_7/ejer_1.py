#1) Hacer una clase Teléfono con los atributos marca, modelo y costo mensual y un método que muestre (o devuelva) el costo anual.

class telefonos:
    def ponerTelefono (self, marca,modelo,costoMensual):
        self.marca=marca
        self.modelo=modelo
        self.costoMensual=costoMensual
    def costoAnual(self):
        return self.costoMensual * 12

untelefono=telefonos()  
untelefono.ponerTelefono("nokia","1234",2)
print(untelefono.costoAnual())


        
    