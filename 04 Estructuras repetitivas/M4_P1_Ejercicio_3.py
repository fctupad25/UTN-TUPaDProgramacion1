# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1= int(input("Introduce un número entero: "))             # Solicita al usuario un numero
num2= int(input("Introduce otro número entero: "))           # Solicita al usuario un numero

minimo = min(num1, num2)                                     # Valor inicial
maximo = max(num1, num2)                                     # Valor final

inicio = minimo +1
suma = 0

while inicio < maximo:
    suma = suma + inicio
    inicio += 1     

print(f"La suma de los números enteros comprendidos entre los valores ingresados es de {suma}")
