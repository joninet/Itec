from dataclasses import dataclass

@dataclass
class Video:
    nombre:str
    visualizaciones: int
    actores: str

@dataclass
class Peliculas(Video):
    minutos: int

@dataclass
class Series(Video):
    temporadas: int

@dataclass
class appVideo:
    listaPeliculas=[]
    listaSeries=[]