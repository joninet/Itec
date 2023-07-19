listaNom=[]
listaSex=[]
def ingreso(nombre, sexo):
    for x in range(2):
      nombre.append(input("ingresar nombre: "))
      sexo.append(input("ingresar sexo M/F: "))
def buscarSex (nombre, sexo):
  buscador=input("ingresar sexo a buscar M/F:")
  nomEncontrado=""
  for rec in range(len(listaSex)):
    busco=listaSex[rec]
    if busco == buscador:
      nomEncontrado+=listaNom[rec]+"-"
      return nomEncontrado[:-2]
      
print(ingreso(listaNom, listaSex))
print(buscarSex(listaNom, listaSex))