# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.


# Leer y mostrar productos del archivo productos.txt
import os

# Ruta absoluta de la carpeta donde está este script (.py)
carpeta = os.path.dirname(os.path.abspath(__file__))

# Armar la ruta completa del archivo productos.txt
ruta = os.path.join(carpeta, "productos.txt")

# Cargar productos desde el archivo en una lista de diccionarios

productos = []  # Lista vacía donde guardaremos los diccionarios

with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()  # Eliminar salto de línea
        if linea:  # Evitar líneas vacías
            nombre, precio, cantidad = linea.split(",")
            
            # Crear un diccionario para cada producto
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            
            # Agregarlo a la lista
            productos.append(producto)

# Mostrar los productos cargados
print("Lista de productos cargada:")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
