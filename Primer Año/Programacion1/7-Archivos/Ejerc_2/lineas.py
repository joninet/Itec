def insertarContenido(archy, posi, textoAinsertar):
    with open(archy) as a:
        t = a.read()
    with open(archy, 'w') as a:
        p = t[:posi] + textoAinsertar + t[posi:]
        print(p)
        a.write(p)

def insertarFila(archy, fila, filaNueva):
     with open(archy) as a:
         lineas = a.readlines()
         filaNueva += '\n'
         lineas.insert(fila-1, filaNueva)
         
     with open(archy, 'w') as a:    
        a.writelines(lineas)

insertarContenido('pruebas/qqq.txt', 6, 'chau')
insertarFila('pruebas/qqq.txt', 2, 'fila nueva')