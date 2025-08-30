# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

edad = int(input("Introduce tu edad: "))            # Solicita al usuario su edad

if  edad > 18:                                     # Compara la edad con la edad minima numeros
    print("Es mayor de edad")
else: 
    print("Es menor de edad")
