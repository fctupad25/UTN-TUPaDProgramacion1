# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = str(input("Introduce tu nombre: "))            # Solicita al usuario su nombre

print("De las siguientes opciones: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. ")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. ")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. ")

opcion = int(input("Introduce la opción que deseada: ")) # Solicita al usuario la opción deseada

resultado = opcion

if   opcion == 1:                                      # Dependiendo de la opción deseada hace la transformacion al nombre
     resultado = nombre.upper()
elif opcion == 2:                                     
     resultado = nombre.lower()
elif opcion == 3:                                     
     resultado = nombre.title()
else: 
     resultado = "La opcion ingresada no es valida"

print(resultado)                                       # Imprime el resultado
