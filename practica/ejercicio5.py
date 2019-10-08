"""
    Práctica 5: funciones anónimas
    @Jorgeflowers18
"""
import math

lista = [(10,2), (8,7), (5,4), (3,11), (10,11)]

raiz = lambda x: math.sqrt(x[0])
potencia = lambda x: pow(x[1], 2)

funciones = lambda x: (raiz(x), potencia(x))
print(list(map(funciones, lista)))
