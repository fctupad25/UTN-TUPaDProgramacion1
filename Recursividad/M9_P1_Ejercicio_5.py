# 5. Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.


def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letras, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si la primera y la última letra son distintas, no es palíndromo
    elif palabra[0] != palabra[-1]:
        return False
    # Paso recursivo: analizar la subcadena interna
    else:
        return es_palindromo(palabra[1:-1])


# Palindromo
texto = input("Ingrese una palabra: ").lower()
print(es_palindromo(texto))


