# 3. Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛 ** 𝑚 = 𝑛 ∗ (𝑛 ** (𝑚−1))
# Prueba esta función en un algoritmo general.

def potencia(n, m):
    if m == 0:             # Caso base
        return 1
    else:                  # Paso recursivo
        return n * potencia(n, m - 1)


# Algoritmo general
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")


