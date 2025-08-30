# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = str(input("Introduce el hemisferio en el que te encuentras (N/S): "))      # Solicita al usuario el hemisferio
mes = int(input("Introduce el mes: "))                                                  # Solicita al usuario el mes
dia = int(input("Introduce el dia: "))                                                  # Solicita al usuario el dia

hemisferio = hemisferio.upper()

if (mes > 0 and mes < 13) and (dia >0 and dia < 31):                                    # Chequea que el dia y mes sea valido

    if  hemisferio == 'N':                                                              # Determina hemisferio en el que se encuentra (N/S)
        
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):        
            print("Invierno")
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            print("Primavera")    
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            print("Verano")
        else: 
            print("Otoño")    

    elif hemisferio == 'S': 
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            print("Verano")
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            print("Otoño")    
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            print("Invierno")
        else: 
            print("Primavera") 

else: 
        print("Datos invalidos") 
