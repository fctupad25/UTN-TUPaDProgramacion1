# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

# Leer y agregar productos al archivo productos.txt
import os

# Ruta absoluta de la carpeta donde está este script (.py)
carpeta = os.path.dirname(os.path.abspath(__file__))

# Armar la ruta completa del archivo productos.txt
ruta = os.path.join(carpeta, "productos.txt")

# Buscar producto por nombre en la lista de diccionarios
productos = []

# Paso 1: cargar los productos desde el archivo
with open(ruta,  "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            nombre, precio, cantidad = linea.split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)

# Paso 2: pedir al usuario el nombre a buscar
buscado = input("Ingresá el nombre del producto que querés buscar: ").lower()

# Paso 3: buscar el producto en la lista
encontrado = False  

for p in productos:
    if p["nombre"].lower() == buscado:
        print(f"Producto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break  # no sigue buscando

# Paso 4: si no se encontró, mostrar mensaje de error
if not encontrado:
    print("El producto no existe en la lista.")
