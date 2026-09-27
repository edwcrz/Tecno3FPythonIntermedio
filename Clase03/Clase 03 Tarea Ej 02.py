# Clase 03 Tarea Ejercicio 02
"""
Escribe un programa que intente sumar un número y una cadena. 
Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
"""
a = 5
cadena = "hola tecno3f"

try:
    resultado = a + cadena
except TypeError as t:
    print (f'se produjo un error por operar con dos tipos de datos diferentes. Error TypeError: {t}')
except Exception as e:
    print (f'se produjo un error de tipo indefinido: {e}')
else:
    print (f'el resultado es: {resultado}')
finally:
    print (f'saludos a Tecno3f')
