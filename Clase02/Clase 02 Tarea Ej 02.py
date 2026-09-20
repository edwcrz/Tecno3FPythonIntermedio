# Ejercicio 02

"""
Dados dos conjuntos A y B, escribe un programa en python que imprima: 
los elementos que se encuentran en A y en B
"""
dias_finde = set()
dias_finde = {"sábado", "domingo"}

dias_laborales = set()
dias_laborales = {"lunes", "martes", "miércoles", "jueves", "viernes"}

semana = dias_laborales.union(dias_finde)
print(f"Días de la semana: {semana}")

## imprimir los hash de los elementos del conjunto
for dia in semana:
    print(f"Hash de {dia}: {hash(dia)}")

print (f"Hash del conjunto semana: {hash("viernes")}")