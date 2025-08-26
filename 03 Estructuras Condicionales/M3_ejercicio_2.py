# Ejercicio 2: Identificador de vocales

letra_usuario = input("Introduce una letra: ") 
letra_usuario = letra_usuario.upper() 


if letra_usuario in ['A', 'E', 'I', 'O', 'U']:
    print("La letra ingresada es una vocal")
else:
    print("La letra ingresada no es una vocal")


# Preguntas de reflexión:
# 1) ¿Cómo manejarías vocales acentuadas (á, é)?    

# if letra_usuario in  ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú']:

# 2) ¿Qué estructura usarías para simplificar las comparaciones?

# Transformaria la letra a mayuscula o minuscula y una lista para captar mas posibilidades.
