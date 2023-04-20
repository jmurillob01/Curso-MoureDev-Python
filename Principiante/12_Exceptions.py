import os
os.system("cls")

### Exceptions ###

try:
    print(5 + 5)
except:
    print("error")
else:
    print("No error")
finally:
    print("Fin de la ejecución")
    
# Excepciones por tipo

try:
    print(5 + "54")
except TypeError as error:
    print(f"Error de TypeError: \n {error}")