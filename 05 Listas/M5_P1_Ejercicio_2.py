# Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.


# Lista vacía
productos = []

# Ingreso 5 productos
for i in range(5):
    producto = input("Ingrese el producto: ")
    productos.append(producto)

# Lista ordenada alfabéticamente
print("Lista de productos ordenada:")
print(sorted(productos))

# Preguntar qué producto eliminar
eliminar = input("Ingrese el producto que desea eliminar: ")


# Chequeo que exista el producto a eliminar
if eliminar in productos:
    productos.remove(eliminar)
    print("Producto eliminado. Lista actualizada:")
    print(sorted(productos))
else:
    print("Ese producto no está en la lista.")
