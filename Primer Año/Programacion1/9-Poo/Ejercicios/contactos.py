"""Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones

Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda"""

from dataclasses import dataclass
from validaciones import*

@dataclass
class Contact:
    id: int
    name: str
    phone: int
    email: str

class App:
    contactList=[Contact(id=1, name='Jonathan', phone=3584249046, email='joninet@msn.com'), Contact(id=2, name='Fernanda', phone=3584155151, email="fernandaalbornoz13@gmail.com")]
    def AddContact(self):
        name=input("Enter the name: ")
        phone=validPhone("Enter the Phone: ")
        email=validEmail("Enter the Email: ")
        contactId=len(self.contactList) + 1
        contact=Contact(contactId,name,phone,email)
        self.contactList.append(contact)

    def showList(self):
        print("Contact list")
        for x in self.contactList:
            print(f"Id: {x.id}, Name: {x.name}, Phone: {x.phone}, Email: {x.email}")

    def contactSearch(self):
        search=input("Enter name to search: ")
        contador=0
        for x in self.contactList:
            if x.name == search:
                print(f"Id: {x.id}, Name: {x.name}, Phone: {x.phone}, Email: {x.email}")
                contador+=1
        if contador==0:
            print("no search result")

    def modifyContact(self):
        try:
            id=int(input("Enter the contact id: "))
            print("1 - Modify Name")
            print("2 - Modify Phone")
            print("3 - Modify email")
            operation=int(input("Enter the num Modify: "))
            if operation == 1:
                nameNew=input("Enter the new name: ")
                for x in self.contactList:
                    if id == x.id:
                        x.name=nameNew
            elif operation == 2:
                phoneNew=validPhone("Enter the new Phone: ")
                for x in self.contactList:
                    if id == x.id:
                        x.phone=phoneNew
            elif operation == 3:
                emailNew=validEmail("Enter the new Email: ")
                for x in self.contactList:
                    if id == x.id:
                        x.email=emailNew
            else:
                print("Enter a correct number")
        except:
            print("Only integers")
    

