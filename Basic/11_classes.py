### Clases ###
"""
Identificar el código dentro de un ámbito de actuacion
El nombre de la clase se escribe con mayuscula primera
Puede tener constructores
"""

class MyEmptyPerson: 
    pass # Cuando no hace nada

print(MyEmptyPerson())
print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname, alias = "Sin alias"): 
        # (Reservado del sistema para recibir un parametro)init permite crear un constructor 
        self.name = name
        self.surname = surname
        
        #Propiedad pública, se puede acceder a ella desde fuera de la clase, se utiliza para almacenar el nombre completo de la persona, se formatea con el nombre, apellido y alias
        self.full_name = f"{name} {surname} ({alias})"

         # Variable privada, no se puede acceder a ella desde fuera de la clase, solo desde dentro de la clase, se utiliza para proteger la variable de cambios externos, se utiliza el doble guion bajo al inicio del nombre de la variable
        self.__name = name

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Gabriela", "Gutierrez")
print(f"{my_person.name} {my_person.surname}")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()
#print(my_person.__name) No se puede acceder a esta variable, es privada


my_other_person = Person("Gustavo", "Gutierrez", "GUS")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Juan Pimpon JP"
print(my_other_person.full_name)

my_other_person.full_name = 123
print(my_other_person.full_name)