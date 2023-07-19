frase = "Jonathan Desplats"
def cuadro(texto):
    for i in range(len(texto) + 6):
        if i == 0:
          print("╔", end="")
        elif i == len(texto)+5:
          print("╗", end="")
        else:
          print("═", end="")
    print()
    print("║"+"  "+texto+"  "+"║")
    for i in range(len(texto) + 6):
        if i == 0:
          print("╚", end="")
        elif i == len(texto)+5:
          print("╝", end="")
        else:
          print("═", end="")
    print()
cuadro(frase)