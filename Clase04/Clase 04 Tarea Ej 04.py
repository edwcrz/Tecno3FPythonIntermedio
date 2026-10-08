"""
Calcular el promedio de una lista de números usando args y un operador ternario
Imprimir un mensaje de error si no se pasan suficientes argumentos
"""
print("Ingrese una lista de números separados por comas para calcular el promedio:")
promedio = 0.0
try:
    ingreso = input("Ingrese los números: ")
    # numeros = [float(num.strip()) for num in ingreso.split(",") if num.strip()]
    numeros = []
    for num in ingreso.split(","):
        if num.strip():
            numeros.append(float(num.strip()))  
    if len(numeros) < 2:
        raise ValueError("Debe ingresar al menos dos números para calcular el promedio.")
except ValueError as ve:
    print(f"Error: {ve}")
    exit()
except Exception as e:
    print(f"Error inesperado: {e}")
    exit()

# función para calcular el promedio de una lista de números con args y operador ternario
def calcular_promedio(*args):
    if args:
        promedio = sum(args) / len(args)
    else:
        promedio = 0.0
    return promedio

promedio = calcular_promedio(*numeros)
print(f"El promedio de los números ingresados es: {promedio}")