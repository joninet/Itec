from contactos import*
"""Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda"""
def menuOptions():
    print("Options:")
    print("1 - Contact Add")
    print("2 - Contact List")
    print("3 - Contact Search")
    print("4 - Contact Edit")
    print("5 - Back to Menu")
    usuarios=App()
    option=int(input("Enter option number: "))
    validado=False
    try:
        while not validado:
            if option == 1:
                usuarios.AddContact()
                validado=True
            elif option == 2:
                usuarios.showList()
                validado=True
            elif option == 3:
                usuarios.contactSearch()
                validado=True
            elif option == 4:
                usuarios.modifyContact()
                validado=True
            elif option == 5:
                menuOptions()
                validado=True
            else:
                print("Numero fuera de rango")
    except:
        print("Ingresar solo Numeros enteros")
menuOptions()