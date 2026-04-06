### Functions ###

def my_function ():
    print("Esto es una funcion")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5, 10)
sum_two_values(5, 7)
sum_two_values("5", "11")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value: int, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}") #Formateo

print_name("Gabriela", "Gutierrez")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Gabriela", "Gutierrez", "GABS")
print_name_with_default("Gabriela", "Gutierrez")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

    print(text)

print_upper_texts("Hola", "Python", "Gabs")
print_upper_texts("Hola")