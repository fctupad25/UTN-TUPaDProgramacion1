# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.


# Matriz (fila = producto,  columna = día) con ventas de 4 productos durante 7 días

ventas = [
    [10, 17, 9, 98, 20, 18, 14],   # Producto 1
    [37, 77, 8, 6, 10, 76, 9],       # Producto 2
    [20, 25, 22, 1, 24, 30, 28],  # Producto 3
    [8, 96, 10, 41, 15, 45, 9]      # Producto 4
]

# Ventas por cada producto
print("Total vendido por cada producto:")
totales_productos = []
for i in range(len(ventas)):
    total = sum(ventas[i])
    totales_productos.append(total)
    print(f"Producto {i+1}: {total}")


# Día con mayores ventas 
totales_dias = []
for j in range(len(ventas[0])):   # recorre columnas
    suma = 0
    for i in range(len(ventas)):  # suma las filas de esa columna
        suma += ventas[i][j]
    totales_dias.append(suma)

dia_max = totales_dias.index(max(totales_dias)) + 1
print(f"Día con mayores ventas fue el día {dia_max} con un total de {max(totales_dias)} unidades.")


# Producto más vendido
producto_max = totales_productos.index(max(totales_productos)) + 1
print(f"El producto más vendido fue el Producto {producto_max} con {max(totales_productos)} unidades.")
