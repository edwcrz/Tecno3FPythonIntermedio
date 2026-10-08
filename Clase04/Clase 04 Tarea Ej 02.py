"""
Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario
"""
print ("Ingrese una lista de palabras separadas por comas:")
try:
    ingreso = input("Ingrese las palabras: ")
    # palabras = [palabra.strip() for palabra in ingreso.split(",") if palabra.strip()]
    palabras = []
    for palabra in ingreso.split(","):
        if palabra.strip():
            palabras.append(palabra.strip())
    if not palabras:
        raise ValueError("Debe ingresar al menos una palabra.")
except ValueError as ve:
    print(f"Error: {ve}")
    exit()
except Exception as e:
    print(f"Error inesperado: {e}")
    exit()

# función para buscar una palabra en la lista con args y operador ternario
def buscar_palabra(palabra_a_buscar, *args):
    return True if palabra_a_buscar in args else False

palabra_a_buscar = input("Ingrese la palabra a buscar: ").strip()
resultado = buscar_palabra(palabra_a_buscar, *palabras)
print(f"La palabra '{palabra_a_buscar}' {'está' if resultado else 'no está'} en la lista.")