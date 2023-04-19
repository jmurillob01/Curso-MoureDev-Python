import os
os.system('cls')

### Tuples ###

# Conjunto de valores
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (21, 1.56, "Javi", "Murillo") # Pêrmite duplicados
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])

my_tuple
print(my_tuple)

print(my_tuple.count("Javi")) # Encuentra una coincidencia
print(my_tuple.index("Javi")) # En la posición 2

# no se pueden asignar valores en una tupla (Es inmutable)

print(my_tuple + my_tuple) # Se pueden complementar

print(my_tuple[1:3]) # Igual que con List y Strings

my_tuple = list(my_tuple) # Se puede hacer a la inversa también, pero lo suyo es usar el tipo necesitado desde un inicio
print(type(my_tuple))

# del my_tuple # Borra la variable / NameError: name 'my_tuple' is not defined
