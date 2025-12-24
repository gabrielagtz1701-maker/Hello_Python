# Tuples

"""
Tupla es un conunto de valores
No es lo mismo que una lista, estas se definen con []
Las tuplas son inmutables, es decir, son valores constantes 
"""

my_tuple = tuple() # Definir una tupla
my_other_tuple = (35, 60, 30)

my_tuple = (27, 1.65, "Gabriela", "Gutierrez")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Gtz")) # Indica cuantas veces aparece el valor
print(my_tuple.index("Gabriela")) # Donde esta el índice 

#my_tuple[5] = 1.80 'tuple' object does not support item assignment
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])

#Reasigno la tupla a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Guadalupe"
my_tuple.insert(1, "Blanco")
print(my_tuple)

# Reasignar lista a tupla
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple # Borar la tupla
# print(my_tuple) NameError: name 'my_tuple' is not defined