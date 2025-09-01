# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


import random

# Generar un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 1

num = int(input("Ingresa un número entero ente 0 y 9: "))         # Solicita un numero entero


while num != numero_secreto:                                      # Compara el numero ingresado con el secreto
    intentos = intentos + 1                                       # Suma el numero de intentos
    num = int(input("Ingresa un número entero ente 0 y 9: "))     # Solicita un numero entero

print(f"El número secreto era {numero_secreto} y la cantidad total de intentos fue: {intentos}")