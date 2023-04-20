import os
os.system('cls')

### Sets ###

my_set = set() # Es igual que en JS -> Valores únicos
my_other_set = {} # Es un diccionario
print(type(my_set))
print(type(my_other_set))

my_other_set = {"Javi", "Murillo"} # Al tener valores se vuelve set
print(type(my_other_set))

print(len(my_other_set))

for item in my_other_set:
    print(item)
    
my_other_set.add("Nuevo") # no se respeta el orden (JS), no admite repetidos
print(my_other_set)

print("Javi" in my_other_set)
print("Javo" in my_other_set)

my_other_set.remove("Javi")
print(my_other_set)

# Para borrar
# my_other_set.clear()
# print(my_other_set)

print(len(my_other_set))

# del my_other_set 
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Javi", "Murillo"} 

my_list = list(my_set) # También puedo crear una lista a apartir de un set, pero es peligroso por el orden ya que lo desconocemos
print(my_list)

my_other_set = {"Java", "JS", "Python"} # Unir dos sets
my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_set.union(my_other_set)) # Como se permite valores duplicados no pasa nada

print(my_new_set.union({"MySQL"})) # La unión

print(my_new_set.difference(my_set)) # La diferencia