# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.


# Definición de la función
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Llamada a función
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

resultado = celsius_a_fahrenheit(celsius)

print("La temperatura en Fahrenheit es:", round(resultado, 2))
