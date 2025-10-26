# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Ingresar los números separados por espacios
parcial1 = set(input("Ingresá los legajos de los que aprobaron el Parcial 1 (separados por espacio): ").split())
parcial2 = set(input("Ingresá los legajos de los que aprobaron el Parcial 2 (separados por espacio): ").split())

# 1 Aprobaron ambos parciales
print("Aprobaron ambos parciales:", parcial1 & parcial2)

# 2 Aprobaron solo uno de los dos
print("Aprobaron solo uno de los dos:", parcial1 ^ parcial2)

# 3 Aprobaron al menos un parcial
print("Aprobaron al menos un parcial:", parcial1 | parcial2)
