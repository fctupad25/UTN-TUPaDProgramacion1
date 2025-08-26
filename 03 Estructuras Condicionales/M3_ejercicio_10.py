#  Ejercicio 10: Piedra, papel o tijera
#  Objetivo: Implementar lógica de juego con condicionales anidados.

#  Instrucciones:
# 1. Pide al usuario las jugadas del Jugador 1 y Jugador 2 (piedra, papel o tijera).
# 2. Usa la tabla proporcionada para determinar el resultado (ganador o
# empate).
# 3. Imprime: "GANA JUGADOR 1", "GANA JUGADOR 2" o "EMPATE".


jugador1 = input("Jugador 1, elige tu jugada (piedra, papel o tijera): ").lower()       # Solicita al usuario 1 una jugada
jugador2 = input("Jugador 2, elige tu jugada (piedra, papel o tijera): ").lower()       # Solicita al usuario 2 una jugada

if jugador1 == jugador2:                                                                # Determina el resultado de la intereaccion dependiendo de cada jugada elegida o si es una jugada invalida
    print("EMPATE")
elif jugador1 == "piedra":
    if jugador2 == "papel":
        print("GANA JUGADOR 2")
    elif jugador2 == "tijera":
        print("GANA JUGADOR 1")
    else:
        print("Jugada invalida de jugador 2.")

elif jugador1 == "papel":
    if jugador2 == "tijera":
        print("GANA JUGADOR 2")
    elif jugador2 == "piedra":
        print("GANA JUGADOR 1")
    else:
        print("Jugada invalida de jugador 2.")

elif jugador1 == "tijera":
    if jugador2 == "piedra":
        print("GANA JUGADOR 2")
    elif jugador2 == "papel":
        print("GANA JUGADOR 1")
    else:
        print("Jugada invalida de jugador 2.")
else: 
     print("Jugada invalida de jugador 1.")




