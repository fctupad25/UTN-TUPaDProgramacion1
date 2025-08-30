# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.



contrasena = input("Escriba una contraseña de entre 8 y 14 caracteres: ")         # Solicita al usuario una contraseña

longitud_valida = 8 <= len(contrasena) <= 14                                      # Evalúa si la longitud está dentro del rango permitido

if longitud_valida:                                                               # Determina si cumple con las condiciones o no
    print("¡Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")