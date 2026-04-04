# Loops (Bucle, ciclos)

# Sirve pra iterar (repetir) algo.
# Pasar por un mismo codigo varias veces

# while
#Se ejecuta varias veces hasta que cambian las condiciones

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es igual a 10")

if my_condition == 10:
    print("Mi condicion es igual a 10")
else:
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
            print("Mi condicion es 15")
            break
    print(my_condition)
print("La ejecucion continua")

# For
# Itera un listado de elementos, se repite tantas veces como elementos tenga

my_list = [27, 24, 62, 52, 30, 30, 17]

for element in  my_list:
     print(element)

my_tuple = (27, 1.65, "Gabriela", "Gutierrez")

for element in  my_tuple:
     print(element)

my_set = {"Gabriela", "Gutierrez", 27}

for element in  my_set:
     print(element)

my_dict = {"Nombre":"Gabriela", "Apellido":"Gutierrez", "Edad":27, 1:"Python"}

for element in  my_dict:
     print(element)
     if element == "Edad":
          break
else:
    print("El bucle for para mi diccionario a finalizado")

    
for element in  my_dict:
     print(element)
     if element == "Edad":
          continue # Detiene la ejecucion en este punto
     else:
        print("Se ejecuta")
else:
    print("El bucle for para mi diccionario a finalizado")