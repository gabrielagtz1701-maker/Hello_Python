# Strings

my_string = "Mi string"
my_other_string = 'Mi oto String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String \ncon salto de línea" # Salto de línea
print(my_new_line_string)  

my_tab_string = "\tEste es un string con tbulación" # Tabulación o sangría
print(my_tab_string)

my_scape_string = "\tEste es un Sring \n escapado" # Combinación de salto de línea y tabulación
print(my_scape_string)

my_scape_string = "\\tEste es un Sring \\n escapado" #Omite la activación del \
print(my_scape_string)

# Formateo

name, surname, age = "Gaby", "Gtz", 27

print("Mi nombre es: {} {}, y mi edad es: {}".format(name, surname, age))
print("Mi nombre es: %s %s, y mi edad es: %d" %(name, surname, age))
print("Mi nombre es: %s %s, y mi edad es: %d" %(name, surname, 27))
print("Mi nombre es: " + name + " " + surname + ", y mi edad es: " + str(age)) # Método tradicional
print(f"Mi nombre es: {name} {surname}, y mi edad es: {age} ")# Inferencia de datos

# Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f  = language
print(a)
print(e)

# División

language_slice = language [1:3]
print(language_slice)

language_slice = language [1:]
print(language_slice)

language_slice = language [-2]
print(language_slice)

language_slice = language [0:6:2]
print(language_slice)

# Reverse

reversed_language = language [::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("2".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())