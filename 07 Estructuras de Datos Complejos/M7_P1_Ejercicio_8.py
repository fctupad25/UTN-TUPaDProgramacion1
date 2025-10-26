# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# Diccionario con productos y su stock
stock = {
    "manzanas": 10,
    "bananas": 5,
    "naranjas": 8
}

# Solicitar un producto al usuario
producto = input("Ingresá el nombre del producto: ").lower()

# Verificar si el producto existe
if producto in stock:
    print(f"El stock actual de {producto} es: {stock[producto]}")

    # Preguntar si quiere agregar más unidades
    agregar = input("¿Querés agregar unidades? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock[producto]}")

else:
    print("El producto no existe en el stock.")
    nuevo = input("¿Querés agregarlo? (s/n): ").lower()
    if nuevo == "s":
        cantidad = int(input("Ingresá la cantidad inicial: "))
        stock[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")

# Mostrar el diccionario final
print("Stock actualizado:")
print(stock)
