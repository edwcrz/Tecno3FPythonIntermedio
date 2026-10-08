"""
Determinar si un número es par o impar
"""
print("Ingrese un número para determinar si es par o impar:")
try:
    ingreso = int(input("Ingrese un número entero: "))
except ValueError as ve:
    print("Error: Debe ingresar un número entero válido.")
    print(f"Detalles del error: {ve}")
    exit()
except Exception as e:
    print(f"Error inesperado: {e}")
    exit()
# Usar un operador ternario para determinar si es par o impar
resultado = "par" if ingreso % 2 == 0 else "impar"
print(f"El número {ingreso} es {resultado}.")
