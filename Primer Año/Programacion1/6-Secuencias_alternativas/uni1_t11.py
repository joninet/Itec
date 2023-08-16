# El costo del pasaje a Córdoba es de $2000. La empresa realiza un descuento de un 40 % sobre el costo del boleto a los niños que tienen entre 5 y 10 años y a los jubilados (mayores de 65). Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.
nom = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 5 and edad <= 10:
    print("Nombre: ",nom)
    print("Edad: ",edad)
    print("Total a pagar con descuento del 40%: $",2000-((2000*40)/100))
elif edad >= 65:
    print("Nombre: ",nom)
    print("Edad: ",edad)
    print("Total a pagar con descuento del 40%: $",2000-((2000*40)/100))
else:
    print("Nombre: ",nom)
    print("Edad: ",edad)
    print("Total a pagar: $2000")