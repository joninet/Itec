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
        print("------------")
        returnSearch()

    def contactSearch(self):
        search=input("Enter name to search: ")
        contador=0
        for x in self.contactList:
            if x.name == search:
                print(f"Id: {x.id}, Name: {x.name}, Phone: {x.phone}, Email: {x.email}")
                contador+=1
        if contador==0:
            print("no search result")
        print("------------")
        returnSearch()

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
        print("------------")
        returnSearch()
def menuOptions():
    print("Options:")
    print("1 - Contact Add")
    print("2 - Contact List")
    print("3 - Contact Search")
    print("4 - Contact Edit")
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
            else:
                print("Numero fuera de rango")
    except:
        print("Ingresar solo Numeros enteros")
def returnSearch():
    print("Options:")
    print("1 - Return")
    print("2 - Exit")
    try:
        option = int(input("Enter option number: "))
        validado = False
        while not validado:
            if option == 1:
                menuOptions()
                validado = True
            elif option == 2:
                validado = True
            else:
                print("Numero fuera de rango")
                option = int(input("Enter option number: "))
    except ValueError:
        print("Ingresar solo números enteros")
menuOptions()