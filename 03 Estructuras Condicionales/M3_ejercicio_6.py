# Ejercicio 6: Detector de años bisiestos
#  Objetivo: Aplicar condiciones compuestas.

#  Instrucciones:
# 1. Pide un año al usuario.
# 2. Si es divisible por 4 pero no por 100, o divisible por 400, imprime: "Se ingresó un año bisiesto".
# 3. En otro caso, imprime: "Se ingresó un año no bisiesto".

anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Se ingresó un año bisiesto.")
else:
    print("Se ingresó un año no bisiesto.")

