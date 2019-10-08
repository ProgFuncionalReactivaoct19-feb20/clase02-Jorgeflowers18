"""
    Práctica 2: funciones anónimas
    @Jorgeflowers18
"""

cadena_personalizada = lambda x, y: ("%s capital de %s" % (x.upper(), y.upper()))
# se modifica a mayusculas las cadenas

print(cadena_personalizada("Cuenca", "Azuay"))