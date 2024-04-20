//Dado un array de números, crea una función que utilice map para duplicar cada número en el array y devolver un nuevo array con los resultados.
let numeros = [1,2,3,4,5,6,7,8,9,10]
const duplicarNum = numeros.map(numero=>numero * 2);
console.log(duplicarNum)

//Dado un array de números, crea una función que utilice filter para filtrar solo los números pares y 
//devolver un nuevo array con esos números.
const numeros = [1,2,3,4,5,6,7,8,9]
let numerosPares = numeros.filter(par => par % 2 === 0)
console.log(numerosPares)

//Dado un array de objetos que representan libros, donde cada objeto tiene las propiedades titulo y autor, crea una función que 
//utilice find para encontrar un libro con un autor específico y devolver ese libro.
let libros = [
    { titulo: "Cien años de soledad", autor: "Gabriel García Márquez" },
    { titulo: "El señor de los anillos", autor: "J.R.R. Tolkien" },
    { titulo: "Orgullo y prejuicio", autor: "Jane Austen" },
    { titulo: "1984", autor: "George Orwell" },
    { titulo: "Harry Potter y la piedra filosofal", autor: "J.K. Rowling" },
    { titulo: "Don Quijote de la Mancha", autor: "Miguel de Cervantes" }
  ];
  let autorBuscar = "Miguel de Cervantes"
  let autor = libros.find(aut => aut.autor === autorBuscar);
  
  console.log(autor)

//Dado un array de personas, donde cada objeto tiene las propiedades nombre y edad, crea una función que utilice map para generar 
//un nuevo array con los nombres de las personas en mayúsculas, luego utilice filter para filtrar solo las personas mayores de 18 años
//, y finalmente utilice find para encontrar la primera persona que tenga exactamente 25 años.
let personas = [
    { nombre: "Juan", edad: 25 },
    { nombre: "María", edad: 30 },
    { nombre: "Pedro", edad: 40 },
    { nombre: "Ana", edad: 35 },
    { nombre: "Luis", edad: 22 },
    { nombre: "Sofía", edad: 28 },
    { nombre: "Carlos", edad: 45 },
    { nombre: "Laura", edad: 17 },
    { nombre: "David", edad: 29 },
    { nombre: "Elena", edad: 16 }
  ];
  let nombreMayuscula = personas.map(mayuscula => mayuscula.nombre.toUpperCase())
  console.log(nombreMayuscula)
  
  let mayoresEdad = personas.filter(mayor => mayor.edad > 18);
  console.log(mayoresEdad)
  
  let encontrar = personas.find(edadVei => edadVei.edad === 25)
  console.log(encontrar)

//Dado un array de objetos que representan productos, donde cada objeto tiene las propiedades nombre, precio y descuento, crea una 
//función para calcular el precio final de cada producto después de aplicar el descuento, luego filtrar solo los productos con un 
//precio final mayor que 50, y finalmente utilice una función para  encontrar el primer producto que tenga un descuento del 20%.
let productos = [
    { nombre: "Camisa", precio: 30, descuento: 10 },
    { nombre: "Pantalón", precio: 50, descuento: 15 },
    { nombre: "Zapatos", precio: 80, descuento: 20 },
    { nombre: "Chaqueta", precio: 100, descuento: 25 },
    { nombre: "Bufanda", precio: 20, descuento: 5 },
    { nombre: "Gorra", precio: 15, descuento: 0 },
    { nombre: "Calcetines", precio: 10, descuento: 0 },
    { nombre: "Reloj", precio: 120, descuento: 30 },
    { nombre: "Bolsa", precio: 40, descuento: 20 },
    { nombre: "Gafas de sol", precio: 60, descuento: 15 }
  ];
  function precioDesc(precio,descuento) {
      const precioTotal = precio - (precio * descuento / 100)
      return precioTotal
  }
  console.log("precios con descuento:")
  for (i=0;i<productos.length;i++){
      console.log(productos[i].nombre + ", Total: $" + precioDesc(productos[i].precio, productos[i].descuento))
  }
  console.log("----------------------")
  console.log("Precios mayor a $50")
  let precioMayor = productos.filter(pMayor => precioDesc(pMayor.precio,pMayor.descuento) > 50)
  console.log(precioMayor)
  console.log("----------------------")
  console.log("Primer Producto con descuento del 20%")
  let descuento = productos.find(desc => desc.descuento === 20)
  console.log(descuento)