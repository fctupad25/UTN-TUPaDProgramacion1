# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha 
# (el último pasa a ser el primero).

lista = [10, 20, 30, 40, 50, 60, 70]

# Ultimo elemento
ultimo = lista.pop()

# Insertarlo en la primera posición
lista.insert(0, ultimo)

print("Lista rotada:", lista)
