# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0
num = int(input("Ingresa un número entero para sumarlo. Ingresa 0 para terminar. "))     # Solicita un numero entero

while num != 0:                                                                         # Mientras no sea cero, seguimos sumando
    suma += num
    num = int(input("Ingresa otro número enteropara sumarlo. Ingresa 0 para terminar. "))

print(f"La suma total es: {suma}")