# Ejercicio 5: Clima según temperatura
#  Objetivo: Clasificar temperaturas en rangos.

#  Instrucciones:
# 1. Pide la temperatura actual en °C.
# 2. Si es ≤ 10°C, imprime: "Hace frío".
# 3. Si está entre 10°C y 25°C, imprime: "Está templado".
# 4. Si es > 25°C, imprime: "Hace calor".

temperatura = float(input("Introduce a temperatura actual: "))     # Solicita al usuario un numero y lo transforma en tipo float

if temperatura <= 10:                                              # Evalua la temperatura
    print("Hace frío")
elif temperatura > 10 and temperatura < 25:
    print("Está templado")
else: 
    print("Hace calor")


