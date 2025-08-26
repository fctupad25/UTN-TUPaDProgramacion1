# Ejercicio 4: Comparador de números
#  Objetivo: Comparar dos números con condicionales.

#  Instrucciones:
# 1. Solicita dos números al usuario.
# 2. Si el primero es mayor, imprime: "El primer número ingresado es mayor".
# 3. Si el primero es menor, imprime: "El primer número ingresado es menor".
# 4. Si son iguales, imprime: "Los números ingresados son iguales".

numero_1 = float(input("Introduce un número: "))            # Solicita al usuario un numero
numero_2 = float(input("Introduce un segundo número: "))    # Solicita al usuario un segundo numero

if numero_1 > numero_2:                                     # Compara ambos numeros
    print("El primer número ingresado es mayor")
elif numero_1 < numero_2:
    print("El segundo número ingresado es mayor")
else: 
    print("Los números ingresadoas son iguales")



#  Preguntas de reflexión:
# 1) ¿Cómo modificarías el programa para comparar más de dos números?

# Agregaria un input para traer un numero extra (num3) y aplicaria una funcion Max() y una Min() para encontrar el numero maximo y minimo entre los ingresados.

# 2) ¿Qué pasa si se ingresan valores no numéricos?

# Similar al ejercicio anterior, el resultado sera error.