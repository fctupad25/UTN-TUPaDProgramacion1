# 6. Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:              # Caso base: un solo dígito
        return n
    else:                   # Paso recursivo: separar último dígito y sumar
        return (n % 10) + suma_digitos(n // 10)


# Ejemplo

num = int(input("Ingrese un número entero positivo: "))
print(suma_digitos(num))


