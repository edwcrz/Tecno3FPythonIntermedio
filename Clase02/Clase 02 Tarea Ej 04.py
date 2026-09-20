# Ejercicio 04

"""
Dado un conjunto A, escribe un programa en python que imprima:
si el conjunto A es un subconjunto de otro conjunto B
"""

A = set()
A = {1,2,3,4,5,6,7,8}

B = set()
B = {5,6,7,8,9,10,11,12,13,14,15}

C = set()
C = {1,2,3,4}   

if (A.issubset(B)):
    print (f"El conjunto A es un subconjunto del conjunto B")
else:
    print (f"El conjunto A no es un subconjunto del conjunto B")

if (C.issubset(A)):
    print (f"El conjunto C es un subconjunto del conjunto A")
else:
    print (f"El conjunto C no es un subconjunto del conjunto A")
