# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

# Diccionario original: país → capital
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

# Crear el nuevo diccionario: capital → país
capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais

# Mostrar el nuevo diccionario
print("Diccionario original (país → capital):")
print(paises)

print("\nDiccionario invertido (capital → país):")
print(capitales)
