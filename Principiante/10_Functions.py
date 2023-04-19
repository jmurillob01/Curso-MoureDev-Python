import os
os.system('cls')

### Functions ###

def my_function():
    print("Función")

my_function()

def suma(first:int, second:int): # El tipado no hace nada
    return first + second

resultado = suma(10, 12)
print(resultado)

def print_name(name, surname): 
    print(f"{name} {surname}")

print_name(surname="murillo", name="javi") # se pueden asignar

def print_name_default(name, surname = ""): # Los valores que no tiene por defecto tienen que ir al final
    print(f"{name} {surname}")
    
print_name_default("Javi")

def print_text(*text):
    print(text)
    
print_text("Hola", "Adios", "a")