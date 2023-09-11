"""Desarrolla una clase Cancion con los siguientes atributos: título y autor y los siguientes métodos: 
constructor que recibe como parámetros el título y el autor de la canción (por este orden). 
dameTitulo(): devuelve el título de la canción. 
dameAutor(): devuelve el autor de la canción. 
 ponerTitulo(String):  establece el título de la canción. 
 ponerAutor(String): establece el autor de la canción. 
"""
class Cancion:
    def __init__(self,Titulo,autorCancion) -> None:
        self.Titulo=Titulo
        self.autorCancion=autorCancion
    def dameTitulo(self):
        return self.Titulo
    def dameAutor(self):
        return self.autorCancion
    
ponerTitulo()