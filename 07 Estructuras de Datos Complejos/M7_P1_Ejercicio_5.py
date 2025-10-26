# Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

# Crear un diccionario vacío para guardar los contactos
contactos = {}

# Cargar 5 contactos (nombre y número)
for i in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input("Ingresá el número de teléfono: ")
    contactos[nombre] = numero

# Consultar un contacto
consulta = input("\nIngresá el nombre del contacto que querés buscar: ")

# Mostrar el número si existe
if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print("Ese contacto no existe en la agenda.")
