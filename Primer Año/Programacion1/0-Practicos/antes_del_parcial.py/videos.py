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
class appVideo:
    listaSeries=[]
    listaPeliculas=[]
    series = [["Peaky Blinders", 1234567, 'Cillian Murphy, Paul Anderson, Helen McCrory', 5],["The Umbrella Academy", 2434908, 'Tom Hopper, Emmy Raver-Lampman, Ellen Page, David Castañeda', 2]]
    pelis = [["Inception", 4760183, 'Leonardo DiCaprio, Ellen Page, Joseph Gordon-Levitt', 148],["Batman Begins", 17319533, 'Christian Bale, Cillian Murphy, Michael Caine', 140],["Inmortales", 35, 'Mirtha Legrand, Leonardo DiCaprio, Elizabeth The Second', 30]]
    for x in series:
        nombre,vis,actores,temp=x
        serie=Series(nombre,vis,actores,temp)
        listaSeries.append(serie)
    for x in pelis:
        nombre,vis,actores,tiem=x
        pelicula=Peliculas(nombre,vis,actores,tiem)
        listaPeliculas.append(pelicula)
    def actorPeliculaLarga(self):
        contador=0
        actor=""
        for i in self.listaPeliculas:
            if i.minutos > contador:
                contador = i.minutos
                actor1=i.actores.split(",")
                actor=actor1[0]
        return f"el actor de la peli mas larga es {actor}"
    def seriesMasdeTres(self):
        seriesLista=[]
        for i in self.listaSeries:
            if i.temporadas > 3:
                seriesLista.append(i.nombre)
        for x in seriesLista:
            print(f"la serie con mas de 3 temporadas {x}")
    def videoMasVisto(self):
        contador=0
        pelicula=""
        for x in self.listaPeliculas:
            if x.visualizaciones > contador:
                contador=x.visualizaciones
                pelicula=x.nombre
        return f"la pelicula mas vista es {pelicula}"

a=appVideo()
print(a.actorPeliculaLarga())
a.seriesMasdeTres()
print(a.videoMasVisto())