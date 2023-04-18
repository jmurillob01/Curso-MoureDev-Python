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
    
my_other_set.add("Nuevo") # no se respeta el orden (JS)
print(my_other_set)

