# Ejercicio 3: Clasificador de números

#  Objetivo: Determinar el signo de un número.

#  Instrucciones:

# 1. Pide un número al usuario.
# 2. Si es positivo, imprime: "El número es positivo".
# 3. Si es negativo, imprime: "El número es negativo".
# 4. Si es cero, imprime: "El número es cero".

numero_usuario = input("Introduce un número: ") 

if numero_usuario > 0:
    print("El número es positivo")
elif numero_usuario < 0:
    print("El número es negativo")
else: 
    print("El número es cero")


# Preguntas de reflexión:
# 1) ¿Qué ocurre si el usuario ingresa un texto?

# En este caso, el resultado sera error.

# 2) ¿Cómo adaptarías el código para números decimales?

# Agregaria un float sobre la variable numero_usuario.