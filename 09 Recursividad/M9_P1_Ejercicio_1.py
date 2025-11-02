# 1. Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):              #Funcion Recursiva
    if n == 0:       
        return 1
    else:                      
        return n * factorial(n - 1)


# Solicitar un número al usuario
num = int(input("Ingrese un número entero: "))

# Calcular y mostrar los factoriales desde 1 hasta num
for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial(i)}")
