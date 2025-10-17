# Crear dos funciones: calcular_area_circulo(radio) que 
# reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro 
# y devuelva el perímetro del círculo. Solicitar el radio al usuario 
# y llamar ambas funciones para mostrar los resultados.


# Función que calcula el área del círculo
pi= 3.14

def calcular_area_circulo(radio):
    return pi * radio ** 2

# Función que calcula el perímetro del círculo
def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

# Llamada a función
radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print("El área del círculo es:", round(area, 2))
print("El perímetro del círculo es:", round(perimetro, 2))
