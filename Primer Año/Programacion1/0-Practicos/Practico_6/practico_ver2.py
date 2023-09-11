class Animal:
    def __init__(self,peso) -> None:
        self.peso=peso
class Puma(Animal):
    def __init__(self,identificador,peso,edad) -> None:
        super().__init__(peso)
        self.identificador=identificador
        self.edad=edad
    def estadoSalud(self):
        if self.peso > 200:
            return f"Sano"
        else:
            return f"enfermo"
    def esAdulto(self):
        if self.edad > 5:
            return f"adultoSi"
        else:
            return f"adultoNo"

class Venado(Animal):
    def __init__(self,identificador,peso) -> None:
        super().__init__(peso)
        self.identificador=identificador
    def estadoSalud(self):
        if self.peso > 120:
            return f"Sano"
        else:
            return f"enfermo"
class Jaula():
    def __init__(self,tipo,carga) -> None:
        self.carga=carga
        self.tipo=tipo
        self.listaJaula=[]
        if tipo == "Puma":
            for x in range(len(self.carga)):
                identificador=x+1
                peso,edad=self.carga[x]
                animal=Puma(identificador,peso,edad)
                self.listaJaula.append(animal)
        elif tipo == "Venado":
            for x in range(len(self.carga)):
                identificador=x+1
                peso=self.carga[x]
                animal=Venado(identificador,peso)
                self.listaJaula.append(animal)
    def obtenerAnimales(self):
        for animales in self.listaJaula:
            salud=animales.estadoSalud()
            print(f"# {animales.identificador} - {salud}")
    def cantidadAdultos(self):
        contador=0
        for animales in self.listaJaula:
            adulto=animales.esAdulto()
            if adulto=="adultoSi":
                contador+=1
        return contador
        


cargaAnimal=[(230, 6), (180, 4), (210, 7), (190, 10)]
jaulaPumas=Jaula("Puma",cargaAnimal)
print("jaula de pumas")
jaulaPumas.obtenerAnimales()
print(f"Cantidad de adultos: {jaulaPumas.cantidadAdultos()}")
cargaAnimal=[100, 130]
jaulaVenados=Jaula("Venado",cargaAnimal)
print("jaula de Venados")
jaulaVenados.obtenerAnimales()