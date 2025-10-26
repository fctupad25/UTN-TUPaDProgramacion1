# Práctico 6: Estructuras de datos complejas

# 1 - Diccionario original
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Mostrar el diccionario 
print(precios_frutas)


# Agregar nuevas frutas con sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar el diccionario actualizado
print(precios_frutas)


# 2 - Actualizar los precios indicados
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el diccionario actualizado
print(precios_frutas)

# 3 - Crear una lista con solo las frutas (las claves del diccionario)
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista
print(lista_frutas)

