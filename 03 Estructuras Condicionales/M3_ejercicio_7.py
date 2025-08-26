# Ejercicio 7: Ajustador de frases
#  Objetivo: Manipular strings con condicionales.

#  Instrucciones:
# 1. Pide una frase o palabra al usuario.
# 2. Si no termina en punto, añádelo al final.
# 3. Imprime el resultado.

frase_palabra = input("Ingresa una frase o palabra: ")

if not frase_palabra.endswith("."):
    frase_palabra += "."

print(frase_palabra)
