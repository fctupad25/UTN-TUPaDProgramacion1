# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente

# Leer y agregar productos al archivo productos.txt
import os

# Ruta absoluta de la carpeta donde está este script (.py)
carpeta = os.path.dirname(os.path.abspath(__file__))

# Armar la ruta completa del archivo productos.txt
ruta = os.path.join(carpeta, "productos.txt")

# Paso 1: Mostrar los productos actuales
print("Productos actuales:")

with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:  # Evita procesar líneas vacías
            nombre, precio, cantidad = linea.split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# Paso 2: Pedir nuevo producto al usuario
print("Ingresar un nuevo producto")
nombre_nuevo = input("Nombre del producto: ")
precio_nuevo = input("Precio: ")
cantidad_nueva = input("Cantidad: ")

# Paso 3: Agregar al archivo sin borrar el contenido (modo 'a')
with open(ruta,  "a", encoding="utf-8") as archivo:
    archivo.write(f"{nombre_nuevo},{precio_nuevo},{cantidad_nueva}\n")

print("Producto agregado correctamente.")
