# 8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.


def contar_digito(numero, digito):
    if numero == 0:                      # Caso base
        return 0
    else:
        ultimo = numero % 10             # Obtener el último dígito
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)   # Sumar 1 y seguir con el resto
        else:
            return contar_digito(numero // 10, digito)       # Seguir sin sumar

# Apariciones

num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese un dígito (entre 0 y 9): "))

print(contar_digito(num, dig))


