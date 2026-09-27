# Clase 03 Tarea Ejercicio 05
"""
Escribe un programa que intente dividir dos números. 
Si el segundo número es cero, captura la excepción ZeroDivisionError. 
Si el primer número es un número no válido, captura la excepción ValueError. 
En cualquier caso, muestra un mensaje de error al usuario.
"""
def pedir_numero (mensaje):
    while cero:
        try:
            numero = float(input(mensaje))
        except ValueError as v:
           print(f"se debe ingresar un número. Error de ValueError: {v}")
           # continue
        else:
            return numero

def dividir (a, b):
    # while True:
        try:
            division = a / b
        except ZeroDivisionError as zd:
            print(f'ingresó un divisor en 0. Error de ZeroDivisionError: {zd}')
            # break
        else:
            return division



primer_num = pedir_numero("ingrese el primer numero un numero decimal (separado por .): ")
segundo_num = pedir_numero("ingrese el segundo numero un numero decimal (separado por .): ")

division_num = dividir (primer_num, segundo_num)
print (f"el resultado de la división es :{division_num}")


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