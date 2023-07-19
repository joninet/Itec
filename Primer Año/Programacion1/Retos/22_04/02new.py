from random import choice
acJugador = 0
acMaquina = 0
while acJugador <= 2 and acMaquina <=2:
    print("Tenes ",acJugador," puntos")
    print("La Computadora tiene ", acMaquina," puntos")
    jugador = input("Ingresar piedra/papel/tijera:")
    computadora = choice(['piedra', 'papel', 'tijera'])
    print("la computadora ingresa: ", computadora)
    if jugador == computadora:
        print("Empate")
    elif jugador == "piedra" and computadora ==  "tijera" or jugador == "papel" and computadora == "piedra" or jugador == "tijera" and computadora == "papel":
        acJugador = acJugador + 1
        print("Ganaste partida")
    elif computadora == "piedra" and jugador ==  "tijera" or computadora == "papel" and jugador == "piedra" or computadora == "tijera" and jugador == "papel":
        acMaquina = acMaquina + 1
        print('Perdiste partida')
if acJugador == 3:
    print('GANASTE EL JUEGO')
    print("Tenes ",acJugador," puntos")
    print("La Computadora tiene ", acMaquina," puntos")
elif acMaquina == 3:
    print('PERDISTE EL JUEGO')
    print("Tenes ",acJugador," puntos")
    print("La Computadora tiene ", acMaquina," puntos")