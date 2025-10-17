# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definición de la función
def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy " + nombre + " " + apellido + ", tengo " + edad + " años y vivo en " + residencia + ".")

# Llamada a función
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

