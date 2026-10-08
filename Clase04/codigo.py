import time
from functools import lru_cache, wraps

#Le realize un ajuste al script para que puedan ver el uso del cache de mejor manera

def medir_tiempo(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
        return resultado
    return wrapper

@medir_tiempo
@lru_cache(maxsize=None)
def encontrar_primos(cantidad):
    primos = [2]
    num = 3
    while len(primos) < cantidad:
        es_primo = True
        for divisor in primos:
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
        num += 2
    return tuple(primos)  # Se retorna como tupla para evitar mutaciones externas

encontrar_primos(10000) # la primer llamada calculara los primos
encontrar_primos(10000) # la segunda llamada consultara el cache y terminara mas rapido