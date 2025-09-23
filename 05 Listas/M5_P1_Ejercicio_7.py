# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.


# Matriz con temperaturas mínimas y máximas (7 días)
temperaturas = [
    [12, 22],  # Día 1
    [18, 27],  # Día 2
    [14, 25],  # Día 3
    [13, 21],  # Día 4
    [11, 23],  # Día 5
    [15, 26],  # Día 6
    [9, 12]    # Día 7
]

# Listas separadas
minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]

prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)

print(f"Promedio de mínimas: {prom_min:.2f}")
print(f"Promedio de máximas: {prom_max:.2f}")


# Amplitud = máxima - mínima
amplitudes = [dia[1] - dia[0] for dia in temperaturas]

mayor_amp = max(amplitudes)
dia_mayor_amp = amplitudes.index(mayor_amp) + 1  

print(f"La mayor amplitud térmica fue de {mayor_amp}°C el día {dia_mayor_amp}.")
