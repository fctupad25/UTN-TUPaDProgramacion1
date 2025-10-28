# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

import os

# Ruta absoluta de la carpeta donde está este script (.py)
carpeta = os.path.dirname(os.path.abspath(__file__))

# Armar la ruta completa del archivo productos.txt
ruta = os.path.join(carpeta, "productos.txt")

with open(ruta, "w", encoding="utf-8") as archivo:
    productos = [
        "pan,500,20",
        "leche,1200,15",
        "arroz,950,10"
    ]
    for producto in productos:
        archivo.write(producto + "\n")

print("Archivo 'productos.txt' creado.")


