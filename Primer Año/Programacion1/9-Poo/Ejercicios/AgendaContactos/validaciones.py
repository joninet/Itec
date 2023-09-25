def validPhone(msg):
    validado=False
    while not validado:
        try:
            phone=int(input("Enter the phone: "))
            validado=True
        except:
            print("Enter valid number")
    return phone

def validEmail(msg):
    validado=False
    while not validado:
        email=input("Enter the Email: ")
        if "@" in email and "." in email:
            validado=True
            print("successfully added")
        else:
            print("Invalid Email")
    return email
