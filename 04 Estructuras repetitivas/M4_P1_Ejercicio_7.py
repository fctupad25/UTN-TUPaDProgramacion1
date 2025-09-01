# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.


num1= int(input("Introduce un número entero: "))           # Solicita al usuario un numero

minimo = 0                                                 # Valor inicial            
suma = 0

while minimo < num1:
    suma = suma + minimo
    minimo += 1     

print(f"La suma de los números enteros comprendidos entre 0 y el valor ingresado es de {suma}")


