"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True: 
    user_input = input("")
    words = user_input.split(" ")
    num1 = int(words[1])
   
    num2 = int(words[2])
    #while True: 

    if words[0] == 'q':
        break
    else:
        if words[0] == "+":
           print(add(num1, num2))
        elif words[0] == "-":
           print(subtract(num1, num2))
        elif words[0] == "*":
           print(multiply(num1, num2))
        elif words[0] == "/":
            print(divide(num1, num2))
        elif words[0] == "square":
            square(num1)
        elif words[0] == "cube":
            cube(num1)
        elif words[0] == "power":
            power(num1, num2)
        elif words[0] == "mod":
            mod(num1, num2)
        else:
            print("I'm sorry I didn't understand that. Please try again.")    
   
   
# Your code goes here
