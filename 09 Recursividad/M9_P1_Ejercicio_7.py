# 7. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide

def contar_bloques(n):
    if n == 1:              # Caso base: la cima tiene un solo bloque
        return 1
    else:                   # Paso recursivo: sumar el nivel actual más los superiores
        return n + contar_bloques(n - 1)


# Cantidad de Bloques
nivel_inferior = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
total = contar_bloques(nivel_inferior)

print(f"Se necesitan {total} bloques para construir la pirámide.")



