# El costo del pasaje a Córdoba es de $2000. La empresa realiza un descuento de un 40 % sobre el costo del boleto a los niños que tienen entre 5 y 10 años y a los jubilados (mayores de 65). Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.
#Modificar este programa para que sirva para una cantidad variable de pasajeros.
#Para ello, el programa debe preguntar si hay más pasajeros. En caso afirmativo volver a solicitar todos los datos y mostrar para cada uno el nombre y el valor del boleto.
#Cuando la respuesta sea NO, el programa termina.

pasajeros = "si"
while pasajeros == "si":
    nom = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    descuento = 2000 - (2000 * 0.40)

    if edad >= 5 and edad <= 10 or edad >= 65:
        print("Nombre: ",nom)
        print("Edad: ",edad)
        print("Total a pagar con descuento del 40%: $ ",descuento)
    else:
        print("Nombre: ",nom)
        print("Edad: ",edad)
        print("Total a pagar: $2000")
    pasajeros = input("mas pasajeros: ")
