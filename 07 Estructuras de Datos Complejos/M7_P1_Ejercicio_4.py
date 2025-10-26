# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# Solicitar una frase al usuario
frase = input("Ingresa una frase: ")

# Separar la frase en palabras
palabras = frase.split()

# Palabras únicas
palabras_unicas = set(palabras)
print("Palabras únicas:")
print(palabras_unicas)

# Contar cuántas veces aparece cada palabra
frecuencias = {}

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

print("Cantidad de veces que aparece cada palabra:")
print(frecuencias)
