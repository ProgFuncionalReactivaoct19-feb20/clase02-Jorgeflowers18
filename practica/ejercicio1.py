"""
    Práctica 1: funciones anónimas
    @Jorgeflowers18
"""

num = int(input("Ingrese número a determinar:\n"))

deter = lambda x: x % 2 == 0 # funcion anónima que divide el número recibido para 2
# así determina si es par o no

print(deter(num)) # se imprime el resultado
