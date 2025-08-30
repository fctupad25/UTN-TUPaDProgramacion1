# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase_palabra = input("Ingresa una frase o palabra: ")   # Solicita al usuario una palabra o frase
frase_palabra_upper = frase_palabra.upper()               # La transforma en mayuscula para evitar errores por case sensitivity


if  frase_palabra_upper[-1] in ['A', 'E', 'I', 'O', 'U']:           # Evalua si la frase termina en vocal y agrega signo de exclamación al final
    print(frase_palabra + "!")
else: 
    print(frase_palabra)



