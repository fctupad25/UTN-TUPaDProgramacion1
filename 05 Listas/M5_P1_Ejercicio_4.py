# Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.
 

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Lista vacía
sin_repetidos = []  

# Chequeo que existan elementos repetidos
for i in datos:
    if i not in sin_repetidos:   
        sin_repetidos.append(i)

print("Lista sin repetidos:", sin_repetidos)
