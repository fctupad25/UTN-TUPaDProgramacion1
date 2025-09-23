# Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.


import random

# Lista con 15 números enteros al azar entre 1 y 100
lista_numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista original de números:", lista_numeros)

# Listas de pares e impares
pares = []
impares = []

for n in lista_numeros:
    resto = n % 2  
    if resto == 0:
        pares.append(n)
    else:
        impares.append(n)

# Mostrar cuántos números tiene cada lista
print("Números pares:", pares)
print("Cantidad de números pares:", len(pares))

print("Números impares:", impares)
print("Cantidad de números impares:", len(impares))
