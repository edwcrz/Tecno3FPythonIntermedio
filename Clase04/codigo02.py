import functools
import time

TOTAL_ELEMENTOS = 100000000
listita = list(range(TOTAL_ELEMENTOS))

def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        fin = time.perf_counter()
        duracion = fin - inicio
        print(f"[{funcion.__name__}] demoró {duracion:.5f} segs")
        return resultado
    return wrapper

def monitorear_acceso_in(paso=2000000):
    def decorador(funcion):
        @functools.wraps(funcion)
        def wrapper(*args, **kwargs):
            global listita
            original = listita
            total = len(original)
            
            def iterador_espia():
                for idx, item in enumerate(original):
                    if idx > 0 and idx % paso == 0:
                        print(f"Inspeccionando índice {idx:,} de {total:,}...")
                    yield item

            listita = iterador_espia()
            try:
                return funcion(*args, **kwargs)
            finally:
                listita = original 
        return wrapper
    return decorador

@medir_tiempo
@monitorear_acceso_in(paso=2000000)
def procesar_datos(buscar):
    return buscar in listita

procesar_datos(-1)