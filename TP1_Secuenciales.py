# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("hola mundo")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

# Usamos la función input para pedirle al usuario que ingrese su nombre

nombre = input("Por favor, escribe tu nombre: ")

# Usamos print para mostrar un mensaje personalizado

print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Escribe tu nombre: ")
apellido = input("Y tu apellido? ")
edad = input("¿Cuántos años tienes? ")
residencia = input("¿Cuál es tu lugar de residencia? ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = float(input("Escribe el radio de un círculo: "))

area = 3.14 * (radio**2)
perimetro = 2 * 3.14 * radio

print(f"El área de un círculo de radio {radio} es de {area} y su perimetro es de {perimetro}.")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = float(input("Escribe una cantidad de segundos: "))

minutos = segundos / 60
horas = round(minutos / 60,2)

print(f"Los segundos ingresados equivalen a {horas} horas.")


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = int(input("Escribe un número: "))

print(f"\nTabla de multiplicar del {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.


num1 = int(input("Escribe un numero entero mayor a 0: "))
num2 = int(input("Escribe un numero entero  mayor a 0: "))

suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2
resta = num1 - num2

print(f"La suma de los números es {suma}.")
print(f"La division de los números es {division}.")
print(f"La multiplicacion de los números es {multiplicacion}.")
print(f"La resta de los números es {resta}.")


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. 

altura = float(input("Escribe tu altura en metros: "))
peso = float(input("Escribe tu peso en kilos: "))

imc = round(peso / (altura)**2,2)

print(f"Su índice de masa corporal es {imc}.")



# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.

tempc = float(input("Escribe una temperatura en grados Celsius: "))

tempf = round(9/5* tempc + 32 ,2)

print(f"La temperatura en grados Fahrenheit es {tempf}.")



# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.


num1a = int(input("Escribe un números: "))
num2a = int(input("Escribe un segundo números: "))
num3a = int(input("Escribe un tercer números: "))

promedio = round((num1a + num2a + num3a) / 3,2)

print(f"El promedio de los números es {promedio}.")