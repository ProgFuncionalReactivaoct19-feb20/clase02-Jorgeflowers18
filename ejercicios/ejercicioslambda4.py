"""
    Ejemplo 4: uso de funciones lambda
    @Jorgeflowers18
"""

datos = ((30, 1.79),(25, 1.60), (35, 1.68))

dato = lambda x: x[2]
edad = lambda x: x[1]*100

print("%.0f" % edad(dato(datos)))

