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
