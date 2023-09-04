"""6) Crear una aplicación para gestionar un videoclub.
Todos los productos tienen:
Titulo, precio alquiler, plazo(dias), alquilado (si/no)
Género (acción, fantasía, etc), año, director, protagonista
Se mantiene un listado de clientes:
– Nº cliente, nombre, dirección, teléfono, productos alquilados
Se guarda un listado de registros de alquiler:
– Cliente, producto, fecha alquiler, fecha devolución, importe
Crear una aplicación de consola con el siguiente menú:
– Lista productos
– Añadir producto
– Ficha producto
– Lista clientes
– Añadir cliente
– Ficha cliente
– Alquiler producto"""
class Productos:
    def __init__(self, Titulo, Precio, Plazo, estadoAlquiler, Genero, Año, Director, Protagonista):
        self.Titulo = Titulo
        self.Precio = Precio
        self.Plazo = Plazo
        self.estadoAlquiler = estadoAlquiler
        self.Genero = Genero
        self.Año = Año
        self.Director = Director
        self.Protagonista = Protagonista
        self.estadoAlquiler = "no"

    def obtener_info(self):
        return f"Titulo: {self.Titulo}, Precio: {self.Precio}, Plazo: {self.Plazo}, estadoAlquiler: {self.estadoAlquiler}, Genero: {self.Genero}, Año: {self.Año}, Director: {self.Director}, Protagonista: {self.Protagonista}"
class Cliente:
    def __init__(self,numeroCliente,nombreCliente,direccion,telefono):
        self.numeroCliente=numeroCliente
        self.nombreCliente=nombreCliente
        self.direccion=direccion
        self.telefono=telefono
        self.productosAlquilados=[]
    def alquilerProducto(self,producto,fechaAlquiler,fechaDevolucion,importe):
        agrego=producto,fechaAlquiler,fechaDevolucion,importe
        self.productosAlquilados.append(agrego)

    def mostrarProductos(self):
        print(f"Información del cliente:")
        print(f"Número de Cliente: {self.numeroCliente}")
        print(f"Nombre: {self.nombreCliente}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print("\nProductos Alquilados:")
        for alquiler in self.productosAlquilados:
            producto, fecha_alquiler, fecha_devolucion, importe = alquiler
            print(f"Producto: {producto.Titulo}")
            print(f"Fecha de Alquiler: {fecha_alquiler}")
            print(f"Fecha de Devolución: {fecha_devolucion}")
            print(f"Importe: ${importe}")
            print("---------------------------")

# Agregar películas a la lista de productos
productosLista = []
pelicula1 = Productos("Los Vengadores", 3.99, 7, "no", "Acción", 2012, "Joss Whedon", "Robert Downey Jr.")
productosLista.append(pelicula1)
pelicula2 = Productos("El Señor de los Anillos", 4.99, 10, "no", "Fantasía", 2001, "Peter Jackson", "Elijah Wood")
productosLista.append(pelicula2)
pelicula3 = Productos("Matrix", 2.99, 5, "no", "Ciencia Ficción", 1999, "Lana Wachowski", "Keanu Reeves")
productosLista.append(pelicula3)
pelicula4 = Productos("Jurassic Park", 3.49, 7, "no", "Aventura", 1993, "Steven Spielberg", "Sam Neill")
productosLista.append(pelicula4)
#agrego cliente
cliente1=Cliente(1,"joni","Gral bustos 2971","4642446",)
#alquilo pelicula
cliente1.alquilerProducto(productosLista[1],"07/09/1987","09/09/1987",200)
cliente1.alquilerProducto(productosLista[2],"07/09/1987","09/09/1987",200)
#muesto productos
cliente1.mostrarProductos()