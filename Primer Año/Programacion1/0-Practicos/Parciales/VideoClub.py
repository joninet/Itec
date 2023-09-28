from dataclasses import dataclass

@dataclass
class Video:
    nombre:str
    visualizaciones: int
    actores: str

@dataclass
class Peliculas(Video):
    listaPeliculas=[]
    minutos: int

@dataclass
class Series(Video):
    temporadas: int
    listaSeries=[]
    def mostrarVisu(self):
        for x in self.listaSeries:
            print(x.visualizaciones)

@dataclass
class appVideo:
    series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 2]]
    pelis = [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]]
    for x in series:
        nomb,visual,actores,temp=x
        serie=Series(nomb,visual,actores,temp)
        serie.listaSeries.append(serie)

a=appVideo()
b=Series.mostrarVisu()