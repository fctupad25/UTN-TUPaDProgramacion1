# Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.


# Matriz con 3 notas de 5 estudiantes
notas = [
    [7, 8, 6],   # Estudiante 1
    [5, 9, 7],   # Estudiante 2
    [8, 7, 9],   # Estudiante 3
    [4, 6, 5],   # Estudiante 4
    [9, 8, 10]   # Estudiante 5
]

# Separa notas de cada estudiante
print("Notas de estudiantes:")
for fila in notas:                  
    for nota in fila:                
        print(nota, " ")         
    print()   

# Revisar cada estudiante
for i in range(len(notas)):                   
    suma = 0
    for j in range(len(notas[0])):               
        suma += notas[i][j]          
    promedio = suma / len(notas[0])           
    print(f"Estudiante {i + 1}: {promedio}")


# Revisar cada materia
for j in range(len(notas[0])):                   
    suma = 0
    for i in range(len(notas)):               
        suma += notas[i][j]          
    promedio = suma / len(notas)             
    print(f"Materia {j + 1}: {promedio}")