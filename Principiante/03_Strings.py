import os
os.system('cls')

### String ###
my_string = "Mi String"
my_other_string = 'otra String'

## Caracteres ###
my_new_line_string = "Este es un String \n con salto de línea"
print(my_new_line_string)

my_tab_string = "\t String con tabulación"
print(my_tab_string)

my_scape_string = "\\t Este es un String escapado"
print(my_scape_string)

### Formateo de String ###
name, surname, age = "Javi", "Murillo", 21
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Inferencia de datos

### Desempaquetado de caracteres ###
language = 'Python'
a, b, c, d, e, f = language
print(a)
print(b)
print(c)

### División ###
language_slice = language[1:3] # De la 1 a la 3 sin incluir
print(language_slice)

language_slice = language[:3]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2] # Del 0 al 6 saltando cada 2 de rango
print(language_slice)

### Reverse ###
reversed_language = language[::-1]
print(reversed_language)

### Funcines ###
print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count('t'))
print(language.isnumeric())
print(language.isalpha())
