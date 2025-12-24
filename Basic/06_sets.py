# Sets

'''
Tienen como base las listas.
Las listas son insmutables, las tuplas no.
Los sets NO son estructuras ordenadas, su forma de guarda elementos es desordenadas
'''

#Definir un set

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Gabriela", "Gutierrez", 27}
print(type(my_other_set)) # Una vez introducidos los datos, se declara como un set

print(len(my_other_set))

print(my_other_set)
my_other_set.add("Guadalupe")
print(my_other_set)
my_other_set.add("Guadalupe") # Un set no admite datos repetidos
print(my_other_set)

##Verificar si existen o no datos en el set
print("Gabriela" in my_other_set)
print("Gaby" in my_other_set)

my_other_set.remove("Guadalupe") # Eliminar un elemento
print(my_other_set)

my_other_set.clear() # Limpia el set
print(my_other_set)
print(len(my_other_set))

del my_other_set # Elimina el set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Gabriela", "Gutierrez", 27} 
my_list = list(my_set) # Transformar un set a una lista
print(my_list)
print(my_list)
print(my_list[1])

my_other_set = {"Kotlin","Swift","Python"}

my_new_set = my_set.union(my_other_set) # Unir dos sets
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) # Agregar elementos y sets 

print(my_new_set)
print(my_set)
print(my_new_set.difference(my_set)) # Muestra la diferencia de los sets