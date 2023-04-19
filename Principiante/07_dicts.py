import os
os.system('cls')

### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Javi", "Apellido": "Murillo", "Edad": 21}
print(my_other_dict)

for item in my_other_dict:
    print(item, ":", my_other_dict[item])
    
print("\n key/value")
for key, value in my_other_dict.items(): # Importante el .items()
    print(key, ":", value)

my_dict = {
    "Nombre": "Javi",
    "Apellido": "Murillo",
    "Edad": 21,
    "lenguajes": {"python", "js", "java"}
}

for item in my_dict:
    print(item, ":", my_dict[item])
    
print(type(my_dict["lenguajes"]))

print(len(my_dict)) # Las claves

# Al igual que en JS se pueden asignar nuevos valores y sobreescribir los existentes

del my_dict["Nombre"]
print(my_dict)

print("Murillo" in my_dict)
print("Apellido" in my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.values())

# Creación de un nuevo diccionario sin valores, se usa desde la palabra reservada
print(dict.fromkeys(("Apellido", 1)))

my_new_dict = dict.fromkeys(("Apellido", 1)) 
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) # Crea un diccionario a partir de las claves de otro, tiene más sentido esto
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "undefined")
print(my_new_dict)
