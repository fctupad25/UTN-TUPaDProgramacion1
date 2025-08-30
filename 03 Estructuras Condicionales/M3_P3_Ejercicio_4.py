# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.


edad = int(input("Introduce tu edad: "))            # Solicita al usuario su edad

if edad < 12:                           # Revisa que el numero sea menor a 12
    print("Niño/a: menor de 12 años")
elif edad < 18:                         # Revisa que el numero sea menor a 18 y mayor 0 igual a 12
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif edad < 30:                         # Revisa que el numero sea menor a 30 y mayor 0 igual a 18
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
else:                                   # Revisa que el numero sea mayor o igual a 30
    print("Adulto/a: mayor o igual que 30 años.")