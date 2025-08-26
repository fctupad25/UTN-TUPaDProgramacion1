# Ejercicio 1: Validación de contraseña
# Objetivo: Analizar un programa existente que verifica una contraseña.
# Instrucciones:
# 1. Lee el siguiente código y explica qué hace:

contrasena_correcta = "programacion1"                    # La variable toma el valor de la contraseña correcta.

contrasena_usuario = input("Introduce la contraseña: ")  # Se solicita al usuario la contraseña para verificarla.

if contrasena_usuario == contrasena_correcta:            # El programa compara la contraseña correcta con la ingresada por el usuario.
    print("Contraseña correcta. Bienvenido.")            # Si la comparacion da un resultado verdadero, muestra en pantalla el mensaje.
else:
    print("Contraseña incorrecta. Intenta de nuevo.")    # En caso que la contraseña ingresada no es correcta, muestra el mensaje en pantalla.


# Preguntas de reflexión:
#  1) ¿Qué pasa si el usuario ingresa la contraseña con mayúsculas? 
# Rta: La contraseña sera incorrecta ya que python es case sensitive.
#  2) ¿Cómo mejorarías el programa para dar más intentos?
# Rta: Agregando una condicion de bucle (While) para que el codigo se repita mientras la contraseña ingresada sea incorrecta permitiendole al usuario seguir intentando opciones.

