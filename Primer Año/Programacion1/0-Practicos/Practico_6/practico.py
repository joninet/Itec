class Animal:
    def __init__(self,identificador,peso) -> None:
        self.identificador=identificador
        self.peso=peso

class Puma(Animal):
    def __init__(self,identificador,peso,edad) -> None:
        super().__init__(identificador,peso)
        self.edad=edad
    def estadoSalud(self):
        if self.peso >= 200:
            return f"Sano"
        else:
            return f"enfermo"
    def esAdulto(self):
        if self.edad > 5:
            return f"Adulto"
        else:
            return f"Joven"

class Venado(Animal):
    def __init__(self,identificador,peso) -> None:
        super().__init__(identificador,peso)
    def estadoSalud(self):
        if self.peso >= 120:
            return f"Sano"
        else:
            return f"enfermo"

class Jaula:
    def __init__(self,tipoAnimal,carga):
        self.tipoAnimal=tipoAnimal
        self.carga=carga
        self.listaAnimal=[]
        for rec in range(len(carga)):
            if tipoAnimal == "Puma":
                peso,años=carga[rec]
                identificador=rec+1
                animal=Puma(identificador,peso,años)
            elif tipoAnimal == "Venado":
                peso=carga[rec]
                identificador=rec+1
                animal=Venado(identificador,peso)
            self.listaAnimal.append(animal)
    def obtenerAnimales(self):
        datos=[]
        for lista in self.listaAnimal:
            salud = lista.estadoSalud()
            datos.append(f"#{lista.identificador} - {salud}")
        return datos
    def cantidadAdultos(self):
        datos=[]
        for lista in self.listaAnimal:
            años = lista.esAdulto()
            datos.append(años)
        return datos
    
            


        


cargaPumas = [(230, 6), (180, 4), (210, 7), (190, 10)]
cargaVenados = [100, 130]

jaulaPumas = Jaula("Puma", cargaPumas)
jaulaVenados = Jaula("Venado", cargaVenados)

for obtener in jaulaPumas.obtenerAnimales():
    print(obtener)
contador=0
for contar in jaulaPumas.cantidadAdultos():
    if contar == "Adulto":
        contador+=1
print(f"cantidad de adultos: {contador}")
print("---")
for obtener in jaulaVenados.obtenerAnimales():
    print(obtener)




    