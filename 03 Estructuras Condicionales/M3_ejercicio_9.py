# Ejercicio 9: Mejorando mensajes de error
#  Objetivo: Dar retroalimentación específica al usuario.
#  Instrucciones:
# 1. Basado en el Ejercicio 8, mejora los mensajes de error:
# o Si tiene <8 caracteres: "La contraseña no es segura. Debe tener al
# menos 8 caracteres.".
# o Si tiene >20 caracteres: "...no más de 20 caracteres.".
# o Si falta mayúscula: "...al menos una mayúscula.".
# o Si falta número: "...al menos un número.".


contrasena_segura = input("Crea la contraseña: ")                               # Solicita al usuario una contraseña

longitud_valida = 8 <= len(contrasena_segura) <= 20                             # Evalua la contraseña
tiene_mayuscula = any(caracter.isupper() for caracter in contrasena_segura)
tiene_numero = any(caracter.isdigit() for caracter in contrasena_segura)

if longitud_valida and tiene_mayuscula and tiene_numero:                        # A partir de la evaluacion determina puntos a mejorar o si es segura
    print("¡Felicitaciones! Creaste tu contraseña.")

else:
    print("La contraseña no es segura.")

    if len(contrasena_segura) < 8:
        print("Debe tener al menos 8 caracteres.")
    
    if len(contrasena_segura) > 20:
        print("No debe tener más de 20 caracteres.")
    
    if tiene_mayuscula == False:
        print("Debe contener al menos una mayúscula.")
    
    if tiene_numero == False:
        print("Debe contener al menos un número.")
    

