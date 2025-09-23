# Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja

# Lista con las notas de 10 estudiantes
notas = [3, 1, 6, 9, 6, 10, 4, 9, 4, 9]

# Lista completa
print("Notas de los estudiantes:", notas)

# Promedio
promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)

# Nota más alta y más baja
nota_max = max(notas)
nota_min = min(notas)
print("Nota más alta:", nota_max)
print("Nota más baja:", nota_min)
