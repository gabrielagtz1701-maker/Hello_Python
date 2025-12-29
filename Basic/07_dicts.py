# Diccionarios 

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Clave : valor
my_other_dict = {"Nombre":"Gabriela", "Apellido":"Gutierrez", "Edad":27, 1:"Python"}
print(type(my_other_dict))
print(my_other_dict)

#Formateo para verlo de forma visual
my_dict = {
    "Nombre":"Gabriela", 
    "Apellido":"Gutierrez", 
    "Edad":27, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.65
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Caracteristica principal, facilidad para acceder a los valores
print(my_dict["Nombre"])

# Actualizar
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])
print(my_dict[1])

# Anadir valor
my_dict["Calle"] = "Calle G"
print(my_dict)

# Eliminar datos
del my_dict["Calle"]
print(my_dict)

print("Gutierrez" in my_dict) # Aparece False porque busca por clave, no por valor
print("Apellido" in my_dict)

# Operaciones

print(my_dict.items()) # Listado de cada uno de los items
print(my_dict.keys()) # Listado de las claves
print(my_dict.values()) # Listado solo de los valores

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list)) # Crea un diccionario sin valores 
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, ["Guti", "Gaby"]) # Ingresar valores a los elementos
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "S")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(dict.fromkeys(list(my_new_dict.values())))
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))