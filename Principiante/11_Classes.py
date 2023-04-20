import os
os.system('cls')

### Classes ###

# pass -> Para que pase y no de error
class My_Empty_Person:
    pass

print(My_Empty_Person)

class Person:
    def __init__(self, name, surname, private): # Constructor de clase [Self -> Es él] = This
        self.name = name
        self.surname = surname
        self.__private = private # Propiedad privada
    
    def get_private(self):
        print(self.__private)
        
    def walk(self):
        print(f"{self.name} está caminando")
    
my_person = Person("Javi", "Murillo", "Propiedad privada")

my_person.get_private() # Básicamente los getter y setter son métodos, si trabajamos con propiedad privada es igual que JS

my_person.walk()