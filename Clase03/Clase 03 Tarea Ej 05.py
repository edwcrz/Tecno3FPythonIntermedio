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

"""
salida = True
resultado = 0
while salida:
    try:
        dividendo = float(input('ingrese un numero que será el dividendo: '))
        divisor = float(input('ingrese un numero que será el divisor: '))
        resultado = float(dividendo / divisor)
    except ValueError as v:
        print(f"se produjo un error por tipo de dato ValueError: {v}")
        continue
    except ZeroDivisionError as z:
        print(f"se produjo un error de división por cero ZeroDiviisonError: {z}")
        continue
    except TypeError as t:
        print(f"se produjo un error por operación de tipo de datos TypeError: {t}")
    except Exception as e:
        print(f"se produjo un error inesperado Exception: {e}")
    else:
        print(f"el resultado es {resultado}")
        print("pasa por else si se ejecuta sin errores el try")
    finally:
        print("Finally se ejecuta siempre sin importar que ocurrió con la ejecución del try")
        print("Finally sirve para cerrar una conexiòn a un archivo o a un db, para que no quede abierto y no 10se corrompa")

print ("continua el programa")
"""