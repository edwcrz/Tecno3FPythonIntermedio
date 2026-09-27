# Clase 03 Tarea Ejercicio 03
"""
Escribe un programa que intente acceder a una clave que no existe en un diccionario. 
Si se produce una excepción KeyError, captura la excepción y muestra
"""

Calificacion = {"id":"100", "nombre":"Juan", "apellido":"Perez", "nota":10}
try:
    print (f'el id del diccionario de la calificación es {Calificacion["id"]}')
    print (f'el nombre del diccionario de la calificación es {Calificacion["nombre"]}')
    print (f'el apellido del diccionario de la calificación es {Calificacion["apellido"]}')
    print (f'la nota del diccionario de la calificación es {Calificacion["nota"]}')
    print (f'el cabello del diccionario de la calificación es {Calificacion["cabello"]}')
    resultado = int(Calificacion["nota"])
except KeyError as k:
    print (f'se produjo un error por llamar a una clave que no existe. Error KeyError: {k}')
except Exception as e:
    print (f'se produjo un error de tipo indefinido: {e}')
else:
    print (f'el resultado es: {resultado}')
finally:
    print (f'saludos a Tecno3f')
