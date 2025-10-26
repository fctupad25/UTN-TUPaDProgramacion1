# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#     Permití consultar qué actividad hay en cierto día y hora.

# Crear la agenda como un diccionario vacío
agenda = {}

# Cargar algunos eventos de ejemplo
agenda[("lunes", "10:00")] = "Reunión de equipo"
agenda[("martes", "14:00")] = "Clase de programación"
agenda[("miércoles", "09:00")] = "Gimnasio"

# Consultar un evento por día y hora
dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (por ejemplo 10:00): ")

# Buscar en la agenda usando una tupla como clave
if (dia, hora) in agenda:
    print(f"En {dia} a las {hora} tenés: {agenda[(dia, hora)]}")
else:
    print("No hay actividades programadas en ese horario.")