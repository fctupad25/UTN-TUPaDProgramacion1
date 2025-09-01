# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

num_ingresados = 100
suma = 0

for i in range(num_ingresados):
    numero = int(input(f"Ingrese un número entero: "))                  # Solicita un numero entero
    suma += numero      

media = suma / num_ingresados   

print(f"La media de los {num_ingresados} números ingresados es: {media}")
