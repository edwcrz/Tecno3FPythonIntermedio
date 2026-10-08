"""
Calcular el mayor de dos números ingresados por teclado usando un operador ternario
"""
print("Ingrese dos números para determinar cuál es el mayor:")
try:
    ingreso1 = float(input("Ingrese el primer número: "))
    ingreso2 = float(input("Ingrese el segundo número: "))  
except ValueError as ve:
    print("Error: Debe ingresar un número válido.")
    print(f"Detalles del error: {ve}")
    exit()
except Exception as e:
    print(f"Error inesperado: {e}")
    exit()

# Usar un operador ternario para determinar el mayor
mayor = ingreso1 if ingreso1 > ingreso2 else ingreso2
print(f"El mayor de los dos números es: {mayor}")