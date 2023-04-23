import os
os.system("cls")

### Challenges ### 

### Fizz buzz
def fizz_buzz():
    for i in range(1,101,1):
        if(i % 3 == 0 and i % 5 == 0):
            print(f"{i} FizzBuzz")
        elif(i % 3 == 0):
            print(f"{i} Fizz")
        elif(i % 5 == 0):
            print(f"{i} Buzz")
        else:
            print(i)

# fizz_buzz()