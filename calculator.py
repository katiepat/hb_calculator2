"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True: 
    user_input = input(" ")
    words = user_input.split(" ")
    token = words[0]

    if len(words) == 2:
        num1 = int(words[1])

    elif len(words) == 3:
        num1 = int(words[1])
        num2 = int(words[2])    

    if token  == 'q':
        break
    else:
        if token  == "+":
           print(add(num1, num2)
        elif token == "-":
           print(subtract(num1, num2))
        elif token == "*":
           print(multiply(num1, num2))
        elif token == "/":
            print(divide(num1, num2))
        elif token == "square":
            print(square(num1))
        elif token == "cube":
            print(cube(num1))
        elif token == "power":
            print(power(num1, num2))
        elif token == "mod":
            print(mod(num1, num2))
        else:
            print("I'm sorry I didn't understand that. Please try again.")    

   
# Your code goes here
