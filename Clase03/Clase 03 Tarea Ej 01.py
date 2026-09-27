# Clase 03 Tarea Ejercicio 01
"""
Escribe un programa que intente dividir dos números. 
Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
"""

try:
    dividendo = float(input("ingrese un numero que será dividendo de una division: "))
    divisor = float(input("ingrese un numero distinto de cero que será el divisor de una division: "))
    resultado = dividendo / divisor
except ZeroDivisionError as z:
    print (f'se está intentando dividir por zero. Error ZeroDivisionError: {z}')
except ValueError as v:
    print(f'no se pudo pasar a numero el valor ingresado. error ValueError: {v}')
except Exception as e:
    print(f'se ingreso un error no identificado: {e}')
else:
    print (f'el resultado es: {resultado}')
finally:
    print("ejecuto finally. Saludos a Tecno3f")