# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, 
# cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

num_ingresados = 100
pares = 0
impares = 0
positivo = 0
negativo = 0
cero = 0

for i in range(num_ingresados):
    num = int(input("Ingresa un número entero: "))      # Solicita un numero entero
    
    if num == 0:
        cero = cero + 1
    else:
       
        if num % 2 == 0:
            pares = pares +1
        else:
            impares = impares +1
        
        if num > 0:
            positivo = positivo +1
        else:
            negativo = negativo +1

print(f"Los numeros ingresados fueron: \n Pares: {pares} \n Impares: {impares}  \n Positivos: {positivo}  \n Negativos: {negativo} \n Ceros: {cero}")


