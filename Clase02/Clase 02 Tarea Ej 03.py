# Ejercicio 03

"""
Dados dos conjuntos A y B, escribe un programa en python que imprima: 
los elementos que se encuentran en A o en B pero no en ambos
"""

A = set()
A = {1,2,3,4,5,6,7,8}

B = set()
B = {5,6,7,8,9,10,11,12,13,14,15}

# Realizo operaciòn de xor entre A y B para obtener los elementos que se encuentran en A o en B pero no en ambos
C = A.symmetric_difference(B)
print (f"Los elementos que se encuentran en A o en B pero no en ambos son: {C}")

