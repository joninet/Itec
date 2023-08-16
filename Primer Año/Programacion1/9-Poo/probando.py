class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca=marca + "probando"
        self.modelo=modelo
        self.camara=camara
    def llamar(self):
        print(f"estas llamando desde un: {self.modelo}")
    def cortar(self):
        print(f"cortaste la llamada desde: {self.modelo}")

celular1=Celular("Samsung", "s23","48MP")
celular2=Celular("Apple", "Iphon 15","50MP")

print(celular1.modelo)
print(celular2.camara)
print(celular1.marca)

celular1.llamar()
celular2.cortar()