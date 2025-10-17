# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.


# Definición de la función
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


# Llamada a función
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

resultado = calcular_promedio(a, b, c)

print("El promedio de los tres números es:", round(resultado, 2))
