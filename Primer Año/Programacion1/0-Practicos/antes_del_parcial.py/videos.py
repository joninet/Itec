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
    self.listaSeries=[]
    self.listaPeliculas=[]
    self.series = [["Peaky Blinders", 1234567, 'Cillian Murphy, Paul Anderson, Helen McCrory', 5],["The Umbrella Academy", 2434908, 'Tom Hopper, Emmy Raver-Lampman, Ellen Page, David Castañeda', 2]]
    self.pelis = [["Inception", 4760183, 'Leonardo DiCaprio, Ellen Page, Joseph Gordon-Levitt', 148],["Batman Begins", 17319533, 'Christian Bale, Cillian Murphy, Michael Caine', 140],["Inmortales", 35, 'Mirtha Legrand, Leonardo DiCaprio, Elizabeth The Second', 30]]