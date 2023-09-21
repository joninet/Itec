from dataclasses import dataclass
@dataclass
class Video:
    nombre: str
    visualizaciones: int
    actores: str

@dataclass
class Series(Video):
    temporadas: int

@dataclass
class Peliculas(Video):
    minutos: int

@dataclass
class Netflix:
    listaSeries=[]
    listaPeliculas=[]
    series = [["Peaky Blinders", 1234567887, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 2]]
    pelis = [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]]
    for x in series:
        nombre,visu,actores,temp=x
        serie=Series(nombre,visu,actores,temp)
        listaSeries.append(serie)
    for x in pelis:
        nombre,visu,actores,min=x
        pelicula=Peliculas(nombre,visu,actores,min)
        listaPeliculas.append(pelicula)
    def mostrar(self):
        for x in self.listaPeliculas:
            print(x.nombre)
    def videoMasVisto(self):
        contador=0
        video=""
        for rec in self.listaPeliculas:
            if rec.visualizaciones > contador:
                contador=rec.visualizaciones
                video=rec.nombre
        for rec in self.listaSeries:
            if rec.visualizaciones > contador:
                contador=rec.visualizaciones
                video=rec.nombre
        return print(f"El video mas visto: {video}")
    def seriesMenosdetres(self):
        print("Series que tienen menos de 3 temporadas:")
        for rec in self.listaSeries:
            if rec.temporadas < 3:
                print(rec.nombre)
    def mismosActores(self):
        actoresPeliculas = []
        print("Actores que trabajan en series y películas:  ")
        for x in self.listaPeliculas:
            actoresP = x.actores.split(",")
            for i in actoresP:
                actoresPeliculas.append(i)
        for x in self.listaSeries:
            actores=x.actores.split(",")
            for i in actores:
                if i in actoresPeliculas:
                    print(i)

            

        
a=Netflix()
a.videoMasVisto()
print()
a.seriesMenosdetres()
print()
a.mismosActores()


