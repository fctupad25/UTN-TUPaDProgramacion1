# Ejercicio 8: Validador de contraseña segura
#  Objetivo: Implementar múltiples condiciones.

#  Instrucciones:
# 1. Pide al usuario que cree una contraseña.
# 2. Verifica que cumpla:
#   o 8+ caracteres y ≤20 caracteres.
#   o Al menos 1 mayúscula (usa .isupper()).
#   o Al menos 1 número (usa .isdigit()).
# 3. Si es segura, imprime: "¡Felicitaciones! Creaste tu contraseña.".
# 4. Si no, imprime: "La contraseña no es segura.".


contrasena_segura = input("Crea la contraseña: ")  

longitud_valida = 8 <= len(contrasena_segura) <= 20
tiene_mayuscula = any(caracter.isupper() for caracter in contrasena_segura)
tiene_numero = any(caracter.isdigit() for caracter in contrasena_segura)

if longitud_valida and tiene_mayuscula and tiene_numero:
    print("¡Felicitaciones! Creaste tu contraseña.")
else:
    print("La contraseña no es segura.")
    

