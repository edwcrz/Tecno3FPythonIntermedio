# Excepciones
"""
Excepciones son errores que ocurren durante la ejecución de un programa.
exceptions son objetos que representan errores y se pueden manejar mediante bloques try-except.
existen diferentes tipos de excepciones, como ValueError, TypeError, IndexError, etc.
las 20 excepciones más comunes en Python son:
mas basicas typeError, indexError, keyError, zeroDivisionError, nameError, attributeError, importError, moduleNotFoundError,
1. Exception, 2. ArithmeticError, 3. BufferError, 4. LookupError, 5. AssertionError, 
6. AttributeError, 7. EOFError, 8. FloatingPointError, 9. GeneratorExit, 10. ImportError, 
11. ModuleNotFoundError, 12. IndexError, 13. KeyError, 14. KeyboardInterrupt, 15. MemoryError, 
16. NameError, 17. NotImplementedError, 18. OSError, 19. OverflowError, 20. RecursionError.

error por ingreso de datos incorrectos, como ingresar un número en lugar de una cadena, se puede manejar con un bloque try-except.
error por división por cero, se puede manejar con un bloque try-except.
error por índice fuera de rango, se puede manejar con un bloque try-except.
error por clave inexistente en un diccionario, se puede manejar con un bloque try-except.
error por la recursividad excesiva, se puede manejar con un bloque try-except.

docs.python.org/3/library/exceptions.html

tupla en python es una estructura de datos que permite almacenar múltiples elementos en un solo objeto. 
Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación. 
Se definen utilizando paréntesis () y los elementos se separan por comas.
"""

"""
# prueba 01
# Type error: ocurre cuando se intenta realizar una operación en un tipo de dato incorrecto.
resultado = 0
try:
    resultado = "Hola" + 5  # Intento de concatenar una cadena con un número
except TypeError as e:
    print(f"Se produjo un TypeError: {e} - No se puede concatenar una cadena con un número.")
    # arrojó: Se produjo un TypeError: can only concatenate str (not "int") to str - No se puede concatenar una cadena con un número.
print (resultado)  # Esto imprimirá 0, ya que la concatenación no se realizó debido al error.
"""

"""
# prueba 02 
# ValueError: ocurre cuando se intenta convertir un valor a un tipo de dato incorrecto.
resultado = 0
try:
    a = 10
    b = int("Hola")  # Intento de convertir una cadena no numérica a entero
    resultado = int(a + b)  # Intento de concatenar una cadena con un número
except ValueError as v:
    print(f"Se produjo un ValueError: {v} - No se puede convertir a entero.")
    # arrojó: Se produjo un ValueError: invalid literal for int() with base 10: 'Hola' - No se puede convertir a entero.
print (resultado)  # Esto imprimirá 0, ya que la conversión no se realizó debido al error.
"""

"""
# prueba 03
# IndexError: ocurre cuando se intenta acceder a un índice que no existe en una lista.
lista = [1, 2, 3]
print(lista[0])  
print(lista[1])
print(lista[2])
    # Esto generará un IndexError porque el índice 5 está fuera del rango de la lista
# print(lista[5])      # Esto generará un IndexError porque el índice 5 está fuera del rango de la lista

lista = [1, 2, 3]
try:
    for i in range(5):
        print(lista[i])  # Esto generará un IndexError porque el índice 5 está fuera del rango de la lista
except IndexError as i:
    print(f"Se produjo un IndexError: {i} - Índice fuera de rango.")
    # arrojó: Se produjo un IndexError: list index out of range - Índice fuera de rango.
print (lista)  # Esto imprimirá la lista original sin cambios
"""

"""
# prueba 04
# KeyError: ocurre cuando se intenta acceder a una clave que no existe en un diccionario
diccionario = {"nombre": "juan", "edad": 30}
try:
    print (diccionario["nombre"])  # Esto imprimirá "juan"
    print(diccionario["edad"])  # Esto imprimirá 30
    print(diccionario["altura"])  # Esto generará un KeyError porque la clave "altura" no existe en el diccionario
except KeyError as k:
    print(f"Se produjo un KeyError: {k} - Clave no encontrada.")
    # arrojó: Se produjo un KeyError: 'altura' - Clave no encontrada.
print(diccionario)  # Esto imprimirá el diccionario original sin cambios
"""

"""
# prueba 05
# ZeroDivisionError: ocurre cuando se intenta dividir un número por cero.
resultado = 0
a = 10
b = 0
try:
    resultado = a / b
except ZeroDivisionError as z:
    print(f"Se produjo un ZeroDivisionError: {z} - No se puede dividir por cero.")
    # arrojó: Se produjo un ZeroDivisionError: division by zero - No se puede dividir por cero.
print(f"El resultado de la división es: {resultado}")  # Esto imprimirá 0, ya que la división no se realizó debido al error.
"""

"""
# prueba 06
# combino ZeroDivisionError y ValueError
resultado = 0
a = 10
b = "hola"
c = 0
d= 1
try:
    resultado = int(a / b)
except ZeroDivisionError as z:
    print(f"se produjo un error de divisiòn por cero ZeroDiviisonError: {z}")
except ValueError as v:
    print(f"se produjo un error por tipo de dato ValueError: {v}")
except TypeError as t:
    print(f"se produjo un error por operación de tipo de datos TypeError: {t}")
except Exception as e:
    print(f"se produjo un error inesperado Exception: {e}")
else:
    print(f"el resultado es {resultado}")
    print("pasa por else si se ejecuta sin errores el try")
finally:
    print("Finnally se ejecuta siempre sin importar que ocurrió con la ejecución del try")
    print("sirve para cerrar una conexiòn a un archivo o a un db, para que no quede abierto y se corrompa")

print ("continua el programa")
"""

"""
# prueba 07
# uso else y finally y continuo
resultado = 0
Escape = True
while Escape:
    try:
        n1 = float(input("ingrese un numero decimal (separado por punto): "))
        n2 = float(input("ingrese un numero decimal (separado por punto): "))
        resultado = n1 / n2
    except ValueError as v:
            print (f"no puedo convertir a float (castear) el tipo de datos que ingresaste (ValueError) {v}")
    except TypeError as t:
        print (f"ingresaste un tipo de datos diferente a float (TypeError) {t}")
    except ZeroDivisionError as z:
        print (f"ingresaste un tipo de datos diferente a float (ZeroDivisionError) {z}")
    except Exception as e:
        print(f"se produjo un error inesperado Exception: {e}")
    else:
        resultado = n1 / n2
        print(f"el resultado es {resultado}")
        print("pasa por else si se ejecuta sin errores el try")
    finally:
        print("Finnally se ejecuta siempre sin importar que ocurrió con la ejecución del try")
        print("sirve para cerrar una conexión a un archivo o a un db, para que no quede abierto y se corrompa")
    print ("continua el programa")
"""

"""
# prueba 08

def pedir_numero (mensaje, cero = True):
    while True:
        try:
            n = float(input(mensaje))
            if not cero and n == 0:
                print("error el divisor no puede ser cero")
                continue
            return n
        except ValueError as v:
            print(f"se debe ingresar un número. Error de ValueError: {v}")

primer_num = pedir_numero("ingrese el primer numero un numero decimal (separado por .): ")
segundo_num = pedir_numero("ingrese el segundo numero un numero decimal (separado por .): ", cero= False)
division_num = primer_num/segundo_num
print (f"el resultado de la división es :{division_num}")
"""

"""
# prueba 09
# creamos una lista con numeros y dos letras que se colaron. la intención era una lista de calificaciones numericas
import datetime
lista_numero = [1, 8, 9, 10, 4, 'a', 2, 3, 'b', 2]
suma = 0
contador = 0


def registrar_error (error, posicion, valor_error):
    ahora = datetime.datetime.now() # tomamos la fecha
    fecha_format = ahora.strftime("%d-%m-%Y-%H-%M-%S")
    print (f"la fecha es :{fecha_format}")
    n_archivo = f'log_error {posicion} {fecha_format}.txt'
    # se puede guardar en archivos independientes como en este caso
    # se podria guardar en un solo archivo de log
    # se podria guardar en una base de datos

    with open (n_archivo, "w") as archivo:
        archivo.write(f'{error} \n')
        archivo.write(f'el valor de la lista en la posicion {posicion} \n')
        archivo.write(f'el valor es {valor_error} \n')

for numero in lista_numero:
    try:
        numero = int(numero)
        suma += numero
        contador += 1
    except Exception as e:
        registrar_error(e, lista_numero.index(numero), numero)
        continue

if contador >0:
    promedio = suma / contador
    print (f"el promedio es {promedio}")
else:
    print ("no se encuentran numeros válidos en la lista")
"""