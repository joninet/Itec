# Recibir por teclado una cadena de números, dejarlo en formato string e insertar  un punto cada 3 dígitos como divisorio de miles. Ej.  “1234567890” debería devolver “1.234.567.890”
numIn = "1234567890"
numNuevo = ""
#          [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
# orden   -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

for i in range(len(numIn)-3, 0, -3):
    #  len=10, 10-3= 7, hasta 0, y que valla de a 3
    print(i)
    numNuevo = numIn[:i] + "." + numIn[i:]
    print(numIn)
    numIn = numNuevo
    #print(numIn)
print(numIn)
