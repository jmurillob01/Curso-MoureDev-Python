import os
os.system('cls')

### Lists ###

my_list = list(["Gato", "Perro", "Ave"])
print(len(my_list))

my_list = ["Gato", "Perro", "Ave"]
print(len(my_list))

my_other_list = [21, 1.55, "Javi", "Murillo"]  # No da error

print(type(my_other_list))

for index, item in enumerate(my_other_list):  # Una manera de recorrer una lista
    print("Index:", index, "Item:", item)

print("------------------")

for item in my_other_list:
    print("Index:", index, "Item:", item)  # Una manera diferente

print(my_other_list.count("Javi"))  # Cuenta el número de ocurrencias

# Desempaquetado
# Tiene que tener el mismo número de elementos que de variables
age, height, name, surname = my_other_list

my_other_list.append("JMB")
print(my_other_list)

# remove elimina la primera coincidencia del array, por valor
# No pongo ejemplo porque es igual que JS

print(my_list)
print(my_list.pop(1))
print(my_list)

# del my_list[1] # Elimina ese elemento de la lista, sin devolver el valor, por índice

my_copy_list = my_list.copy()
print(my_copy_list)

my_copy_list.reverse()
print(my_copy_list)

# sublista
print(my_other_list[1:3])