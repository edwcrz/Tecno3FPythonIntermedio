# Clase 03 Tarea Ejercicio 05
"""
Escribe un programa que intente dividir dos números. 
Si el segundo número es cero, captura la excepción ZeroDivisionError. 
Si el primer número es un número no válido, captura la excepción ValueError. 
En cualquier caso, muestra un mensaje de error al usuario.
"""
def pedir_numero (mensaje):
    while True:
        try:
            numero = float(input(mensaje))
        except ValueError as v:
           print(f"se debe ingresar un número. Error de ValueError: {v}")
           # continue
        else:
            return numero

def dividir (a, b) -> tuple [float, bool]:
    # while True:
        try:
            division = 0
            flag = False
            division = float(a / b)
        except ZeroDivisionError as zd:
            print(f'ingresó un divisor en 0. Error de ZeroDivisionError: {zd}')
            flag = True
            return 0.0, flag
            # break
        else:
            return division, flag

permanecer = True
while permanecer == True :
    ingreso = str(input("ingrese SALIR para salir del programa o ingrese la tecla enter para continuar :"))
    if ingreso == "SALIR":
        permanecer = False
        break
    flag = False
    dividendo = pedir_numero("ingrese un numero decimal como dividendo: ")
    divisor = pedir_numero("ingrese un numero decimal como divisor distinto de cero: ")
    resultado, flag = dividir (dividendo, divisor)
    if flag == False:
        print (f"el resultado de la división es :{resultado}")
    elif flag == True:
        print ('Por favor no ingrese un divisor en cero')
    else:
        print('Saludos a Tecno3f')