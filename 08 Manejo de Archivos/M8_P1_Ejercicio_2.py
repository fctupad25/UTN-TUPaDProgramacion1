# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

# Leer y mostrar productos del archivo productos.txt
import os

# Ruta absoluta de la carpeta donde está este script (.py)
carpeta = os.path.dirname(os.path.abspath(__file__))

# Armar la ruta completa del archivo productos.txt
ruta = os.path.join(carpeta, "productos.txt")

# Abrir archivo en modo lectura ('r')
with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        # Quitamos saltos de línea y espacios al final
        linea = linea.strip()
        
        # Separar los datos por coma -> [nombre, precio, cantidad]
        nombre, precio, cantidad = linea.split(",")
        
        # Mostrar los datos
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
