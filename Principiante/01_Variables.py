import os
os.system('cls')

import operator

# Variables
my_variable = "Primera variable"
print(my_variable)

my_int_variable = (5)
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# En el print podemos añadir diferentes caracteres
print(my_variable, my_int_variable, my_bool_variable)

# Creación para ver el tipo de dato
concatenar = (my_variable, my_int_variable, my_bool_variable)

print(type(concatenar)) # tupla = Array, pero no se puede modificar
print(concatenar[1])

print(len(str(10))) # El len solo funciona con cadenas y con listas

# Variables en una sola línea
name, surname, alias = "Javi","Murillo", "JMB"

# El primer argumento es menor o igual al segundo
print(operator.le(40,20)) 

# first_name = input('Indica cual es tu nombre: ') # No se suele usar mucho
# print("Hola " + first_name)

first_name = 123 # Se puede cambiar el tipo de valor y su contenido
print(first_name)

 # Indicamos el tipado para ayudarnos a entender cual es el tipo de valor, pero no lo fuerza
address: str = "Mi dirección"
address = 31
print(type(address))