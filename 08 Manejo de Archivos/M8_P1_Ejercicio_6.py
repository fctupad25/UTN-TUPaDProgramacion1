# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

# Leer y agregar productos al archivo productos.txt
import os

# Ruta absoluta de la carpeta donde está este script (.py)
carpeta = os.path.dirname(os.path.abspath(__file__))

# Armar la ruta completa del archivo productos.txt
ruta = os.path.join(carpeta, "productos.txt")


# Guardar los productos actualizados en el archivo productos.txt
productos = []

# Paso 1: Leer el archivo y cargar los productos en una lista de diccionarios
with open(ruta, "r", encoding="utf-8") as archivo:
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

# Paso 2: Mostrar los productos actuales
print("Productos actuales:")
for p in productos:
    print(f"{p['nombre']} - ${p['precio']} - {p['cantidad']} unidades")

# Paso 3: Permitir al usuario modificar o agregar un producto
print("Ingresar un nuevo producto o actualizar uno existente")
nombre_nuevo = input("Nombre del producto: ").lower()
precio_nuevo = float(input("Precio: "))
cantidad_nueva = int(input("Cantidad: "))

# Paso 4: Si el producto ya existe, actualizarlo; si no, agregarlo
encontrado = False
for p in productos:
    if p["nombre"].lower() == nombre_nuevo:
        p["precio"] = precio_nuevo
        p["cantidad"] = cantidad_nueva
        encontrado = True
        break

if not encontrado:
    productos.append({
        "nombre": nombre_nuevo,
        "precio": precio_nuevo,
        "cantidad": cantidad_nueva
    })

# Paso 5: Sobrescribir el archivo con la lista actualizada
with open(ruta, "w", encoding="utf-8") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print("Archivo 'productos.txt' actualizado correctamente.")
