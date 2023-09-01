#Desarrolla una clase Cancion con los siguientes atributos: título y autor y los siguientes métodos: 
#constructor que recibe como parámetros el título y el autor de la canción (por este orden). 
#dameTitulo(): devuelve el título de la canción. 
#dameAutor(): devuelve el autor de la canción. 
#ponerTitulo(String):  establece el título de la canción. 
#ponerAutor(String): establece el autor de la canción. 
class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def dameTitulo(self):
        return self.titulo

    def dameAutor(self):
        return self.autor

    def ponerTitulo(self, nuevoTitulo):
        self.titulo = nuevoTitulo

    def ponerAutor(self, nuevoAutor):
        self.autor = nuevoAutor

titulo = "Minutos"
autor = "Ricardo Arjona"
a = Cancion(titulo, autor)

print(a.dameTitulo())
print(a.dameAutor())

    

