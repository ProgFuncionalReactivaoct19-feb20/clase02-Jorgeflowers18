"""
    Práctica 4: funciones anónimas
    @Jorgeflowers18
"""

lista = [10, 2, 8, 7, 5 ,4, 3, 11, 0, 1]

# se eleva al cubo cada elemento en cada iteración
potencia = lambda x: pow(x, 3) 

print(list(map(potencia, lista)))