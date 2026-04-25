### Modules ###

# Librería donde se tiene código reutilizable, como funciones, clases, variables, etc. que se pueden importar y usar en otros archivos de Python.

# Importa el módulo completo, es decir, otro archivo de Python que contiene código reutilizable.

import my_module
my_module.sum(5, 10, 15)
my_module.printValue("Hola, soy un móduloI")


from my_module import sum, printValue
sum(5, 10, 15)
printValue("Hola, soy un móduloI")

import math
print(math.pi)
print(math.pow(2, 3))

from math import pi as PI_VALUE, pow as POW_VALUE
print(PI_VALUE)
print(POW_VALUE(2, 3))