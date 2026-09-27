# Clase 03 Tarea Ejercicio 04
"""
Escribe un programa que intente abrir un archivo que no existe. 
Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario.
Sin embargo, también intenta crear el archivo si no existe.
"""
"""
"r"     read
"w"     write (escribir, crear, sobrescribir)
"a"     append (agregar, crear si no existe)
"x"	    Crear exclusivamente
"r+"    Leer + escribir
open()
json.load()
json.dump()
json.loads()
json.dumps()
"""
import json
"""
datos = {
        "nombre": "Eduardo",
        "edad": 49,
        "lenguajes": ["Python", "SQL"]
        }
"""
try:
    with open("datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
except FileNotFoundError as fe:
    print(f'se registra un error porque el archivo no existe. error FileNotFoundError: {fe}')
    datos = {}
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)
        print(f"Dentro del with: {archivo.closed}")
    print(f"Fuera del with: {archivo.closed}")
except Exception as e:
    print(f'se registra un error desconocido: {e}')
else:
    print(f'el archivo existia')
finally:
    print(f'el archivo json tine la siguiente informacion {datos}')
    archivo.close()
    if archivo.closed:
        print("El archivo está cerrado correctamente.")
    else:
        print("El archivo sigue abierto.")
print("saludos Tecno3F")
    