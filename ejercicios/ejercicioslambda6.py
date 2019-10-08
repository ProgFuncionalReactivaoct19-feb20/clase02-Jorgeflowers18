"""
    Ejemplo 6: uso de funciones lambda
    @Jorgeflowers18
"""

lista = [10, 2, 3, 5, 1]
#anios = lambda x: x[0]
#estatura = lambda x: x[1]

funciones = lambda x: x + 100

print(min(list(map(funciones, lista))))

