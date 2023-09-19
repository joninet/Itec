#El operador ternario es un operador de tres operadores que nos permite evaluar una condición y devolver 
#un valor u otro según el resultado de la evaluación.

#<condición> ? <valor_si_verdadero> : <valor_si_falso>

#el siguiente código usa el operador ternario para evaluar si una variable es mayor que 10:
edad = 18
es_mayor = edad > 10 ? "Es mayor" : "Es menor o igual"
print(es_mayor)

#Podemos usar el operador ternario para escribir un if con un else en una sola línea. Por ejemplo, 
#el siguiente código imprime "Es mayor" si la variable edad es mayor que 10, y "Es menor o igual" 
#si no lo es:

edad = 18
es_mayor = "Es mayor" if edad > 10 else "Es menor o igual"
print(es_mayor)
