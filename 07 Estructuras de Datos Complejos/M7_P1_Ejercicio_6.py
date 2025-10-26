# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

# Diccionario para guardar los alumnos y sus notas
alumnos = {}

# Nombres y Notas
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")

    # Lista temporal para guardar las 3 notas
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)

    # Convertir la lista en tupla 
    alumnos[nombre] = tuple(notas)

# Mostrar el promedio de cada alumno
print("Promedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

