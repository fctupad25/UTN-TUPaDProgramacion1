# 2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(n):     # Fibonacci
    if n == 0:        # Caso base 1
        return 0
    elif n == 1:      # Caso base 2
        return 1
    else:             # Paso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)


# Solicitar un número al usuario
num = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

# Mostrar la serie completa hasta esa posición
print(f"Serie de Fibonacci hasta la posición {num}:")
for i in range(num + 1):
    print(f"{fibonacci(i)}")

