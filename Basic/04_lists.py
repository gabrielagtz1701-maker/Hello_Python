# Lists 

my_list = list()
my_other_list = []

print (len(my_list))

my_list = [27, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [27, 1.65, "Gabriela", "Gtz"]
print(my_other_list)
print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])# Acceder a posiciones o datos específicos
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_list.count(30)) # Retorna el npumero de ocurrencias de un valor

#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list #Definir variables, desempaquetar datos
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)
print(age)

print(my_list + my_other_list)
#print(my_list - my_other_list) TypeError

my_other_list.append("Mouredev") # Añadir un elemento al final de la lista siempre
print(my_other_list)

my_other_list.insert(1,"Rojo") # Insertar un elemento en la lista en una posición definida
print(my_other_list)

my_other_list[1] = "Blanco" # Cambia el valor de la posición dad en la lista 
print(my_other_list)

my_other_list.remove("Mouredev") # Eliminar un elemento
print(my_other_list)

my_list.remove(30) # Elimina el primer valor que encuentra
print(my_list)

my_list.pop() # Elimina el último valor de la lista por defecto
print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2) # Selecciona el elementos a eliminar
print(my_pop_element)
print(my_list)

del my_list[2] # Eliminar elemento por índice
print(my_list)

my_new_list = my_list.copy() # Copia la lista en una nueva variable 

my_list.clear() # Limpiar toda la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # Imprime valores al revés
print(my_new_list)

my_new_list.sort() # Ordena la lista bajo criterios
print(my_new_list)

print(list([1, 2, 3, 4]))
print(type([1, 2, 3, 4]))

#Tipos dinámicos
my_list = list("Hola Python")
my_list = ["Hola Python"]
print(my_list)
print(type(my_list))