#9) Definir una clase Telefono, sus atributos son: marca, modelo, sistema operativo, plan(costo) 
#y cantidad de RAM. Sus métodos son: costo anual, mostrar Sistema Operativo y si es gama alta o no 
#(con 6 o más gigas de RAM) .
class Telefono:
    def __init__(self,marca,modelo,so,plan,ram):
        self.marca=marca
        self.modelo=modelo
        self.so=so
        self.plan=plan
        self.ram=ram
    def costoAnual(self):
        return self.plan * 12
    def Gama(self):
        if self.ram > 6:
            return "Alta"
        else:
            return "Baja"
telefono1 = Telefono("Motorola", "G13", "Android", 3500, 7)
print("Caracteristicas del celular")
print(f"Marca: {telefono1.marca}\nModelo: {telefono1.modelo}\nSistema Operativo: {telefono1.so}\nPlan(costo): {telefono1.plan}\nMemoria Ram: {telefono1.ram} GB.\nCosto mensual: ${telefono1.costoAnual()}\nGama: {telefono1.Gama()}")
