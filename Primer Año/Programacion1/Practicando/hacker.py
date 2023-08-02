abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
hacker = ['4', 'I3', '[', ')', '3', '|=', '&', '#', '1', ',_|', '>|',
            '1', '/\/\\', '^/', '0', '|*', '(_,)', 'I2', '5', '7',
            '(_)', '\/', '\/\/', '><', 'j', '2']

validado=False
while not validado:
    palabra=input("ingresar palabra: ")
    palabra=palabra.lower()
    if palabra.isalpha():
        hackerPal=""
        for x in range(len(palabra)):
            hackerPal = hackerPal + hacker[abc.index(palabra[x])]
        validado=True
        print(hackerPal)
    else:
        print("ingresar solo letras")

