from random import choice
acJugador = 0
acMaquina = 0
jugador = input("Ingresar piedra/papel/tijera:")
computadora = choice(['piedra', 'papel', 'tijera'])
print("la computadora ingresa: ", computadora)
if jugador == computadora:
    print("Empate")

elif jugador == "piedra" and computadora == "tijera" or jugador == "papel" and computadora == "piedra" or jugador == "tijera" and computadora == "papel":
    acJugador = acJugador + 1
    print("Ganaste")
else:
    print("Perdiste")
