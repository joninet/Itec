"Hola Mundo".upper() # 'HOLA MUNDO'
"Hola Mundo".lower() # 'hola mundo'
"hola mundo".capitalize() # 'Hola mundo'
"hola mundo".title() # 'Hola Mundo'
"Hola mundo".count('mundo') # 1
"Hola mundo".find('mundo') # 5
"Hola mundo mundo mundo".rfind('mundo') # 17
c = "100" // c.isdigit() # True
c = "ABC10034po" // c.isalnum() # True
"Holamundo".isalpha() # True
"Hola mundo".islower() # False
"Hola mundo".isupper() # False - Devuelve True si la cadena es todo mayúsculas:
"Hola Mundo".istitle() # True - Devuelve True si la primera letra de cada palabra es mayúscula:
"  -  ".isspace() # Devuelve True si la cadena es todo espacios:
"Hola,mundo,mundo,otra,palabra".split(',') # ['Hola', 'mundo', 'mundo', 'otra', 'palabra']
",".join("Hola mundo") # 'H,o,l,a, ,m,u,n,d,o'
"-----Hola mundo---".strip('-') # 'Hola mundo'
"Hola mundo".replace('o','0') # 'H0la mund0'
