# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Definición de la función
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

# Llamada a función
segundos = int(input("Ingrese la cantidad de segundos: "))

resultado = segundos_a_horas(segundos)

print("Equivalen a", round(resultado, 2), "horas.")
