#Crea una clase Cuenta (bancaria) con atributos para el número de cuenta, el DNI del cliente, el saldo actual y el interés anual que se aplica a la cuenta (porcentaje). 
#Define en la clase los siguientes métodos: constructor con DNI, saldo e interés. 
#Método actualizarSaldo(): actualizará el saldo de la cuenta aplicándole el interés diario (interés anual dividido entre 365 aplicado al saldo actual), 
#método ingresar(float):  permitirá ingresar una cantidad en la cuenta, método retirar(float): permitirá sacar una cantidad de la cuenta (si hay saldo). 
#Finalmente, un método que nos permita mostrar todos los datos de la cuenta. 
class Cuenta:
    def __init__(self, dniCliente, saldoActual, interesAnual):
        self.dniCliente = dniCliente
        self.saldoActual = saldoActual
        self.interesAnual = interesAnual
    def actualizarSaldo(self):
        interes = ((self.interesAnual / 100) / 365) * self.saldoActual
        self.saldoActual += interes
    def depositar(self,cantidadD):
        self.saldoActual += cantidadD
    def retirar(self,cantidadR):
        if self.saldoActual > cantidadR:
            self.saldoActual -= cantidadR
        else:
            print("Cantidad ingresada mayor al saldo")
    def mostrar(self):
        return self.dniCliente, self.saldoActual
    
ingresoCliente=Cuenta(33054148,23000,98)
ingresoCliente.depositar(4000)
ingresoCliente.retirar(2000)
print(ingresoCliente.mostrar())
    
    



    

