# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.


# Matriz 3x3

filas = 3
columnas = 3

matriz = []                  

for i in range(filas):       
    fila = []                
    for j in range(columnas):
        fila.append("-")     
    matriz.append(fila)      

# Casillas vacias
for fila in matriz:
    print(" ".join(fila))

# Jugadas posibles
jugadas = ["X", "O"]

for turno in range(9):
    jugador = jugadas[turno % 2]  
    print(f"Turno del jugador {jugador}")

    # Pedir posición
    fila = int(input("Ingresa la fila (0, 1 o 2): "))
    col = int(input("Ingresa la columna (0, 1 o 2): "))

    # Validar que la casilla esté vacía
    if matriz[fila][col] == "-":
        matriz[fila][col] = jugador
    else:
        print("Posicion ocupada, intenta de nuevo.")
        continue  

    # Mostrar tablero actualizado
    for fila_matriz in matriz:
        print(" ".join(fila_matriz))
    print()