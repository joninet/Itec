"""Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones

Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda"""

from dataclasses import dataclass

@dataclass
class Contact:
    id: int
    name: str
    phone: int
    email: str

class App:
    contactList=[]
    def AddContact(self):
        validado=False
        name=input("Enter the name: ")
        while not validado:
            try:
                phone=int(input("Enter the phone: "))
                validado=True
            except:
                print("Enter valid number")
        validado=False
        while not validado:
            email=input("Enter the Email: ")
            if "@" in email and "." in email:
                contactId=len(self.contactList) + 1
                contact=Contact(contactId,name,phone,email)
                self.contactList.append(contact)
                validado=True
                print("successfully added")
            else:
                print("Invalid Email")
    def showList(self):
        print("Contact list")
        for x in self.contactList:
            print(f"Id: {x.id}, Name: {x.name}, Phone: {x.phone}, Email: {x.email}")
    


usuarios=App()
usuarios.AddContact()
usuarios.AddContact()
usuarios.showList()
