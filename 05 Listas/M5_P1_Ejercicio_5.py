# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

# Lista estudiantes
estudiantes = ["Juan", "Pedro", "Maria", "Juana", "Marta", "Florencia", "Sofía", "Diego"]

print("Lista de estudiantes presentes en clase: ", estudiantes)

# Preguntar cambios en la lista
cambio_lista = input("¿Desea agregar o eliminar un estudiante? (escriba 1 para agregar o 0 para eliminar): ")

# Aplicar cambios en la lista
if cambio_lista == "1":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"{nuevo} fue agregado a la lista.")

elif cambio_lista == "0":
    eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print(f"{eliminar} fue eliminado de la lista.")
    else:
        print(f"{eliminar} no está en la lista.")

else:
    print("Opción no válida. No se hicieron cambios.")

# Lista final actualizada
print("Lista final de estudiantes: ", estudiantes)
