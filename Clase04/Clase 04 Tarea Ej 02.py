"""
Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario
"""
print ("Ingrese una lista de palabras separadas por comas:")
try:
    ingreso = input("Ingrese las palabras: ")
    palabras = [palabra.strip() for palabra in ingreso.split(",") if palabra.strip()]
    if not palabras:
        raise ValueError("Debe ingresar al menos una palabra.")
except ValueError as ve:
    print(f"Error: {ve}")
    exit()
except Exception as e:
    print(f"Error inesperado: {e}")
    exit()