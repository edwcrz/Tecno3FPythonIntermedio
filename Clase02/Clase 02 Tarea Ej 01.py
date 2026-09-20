# Ejercicio 01

"""
Dados dos conjuntos A y B, escribe un programa en python que imprima: 
los elementos que se encuentran en A pero no en B o en ambos
"""
B = set()
# B = {"sábado", "domingo"}
B= {5,6,7,8,9,10,11,12,13,14,15}

A = set()
# A = {"lunes", "martes", "miercoles", "jueves", "viernes"}
A = {1,2,3,4,5,6,7,8,9,10}

# print("Días de fin de semana:", dias_finde)
# print("Días laborales:", dias_laborales)

C = A.intersection(B)
print (f"Los elementos que se encuentran en A y B son: {C}")

D = A.difference(B|C)
print (f"Los elementos que se encuentran en A pero no en B o en ambos son: {D}")

print (f"Los elementos que se encuentran en A pero no en B o en ambos son: {A - B}")
print (f"Los elementos que se encuentran en A pero no en B o en ambos son: {A - (B|C)}")
print (f"Los elementos que se encuentran en A pero no en B o en ambos son: {A.difference(B)}")