### List Comprenhension ###
# The condition is like a filter that only accepts the items that valuate to True.

### Limpiar pantalla ###
import os
os.system("cls")

my_original_list = [0,1,2,3,4,5,6,7,9,10]

my_list = [i for i in my_original_list]
print(my_list)

my_list = [i for i in range(8)] # Más rápido para crear listas numéricas
print(my_list)

my_list = [i for i in range(8) if i >= 4]
print(my_list)

my_list = [print(i) for i in range(8)] # Un ejemplo extraño

