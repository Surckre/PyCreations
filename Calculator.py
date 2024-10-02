# simple calculator in python

# variables
num1 = float(input("Enter ur first Number: ")) # first input
operator = input("Enter ur operator (+ - * /) ") # operator input
num2 = float(input("Enter ur second Number: ")) # second input

# functions
# operator for +
if operator == "+":
  result = num1 + num2
# operator for -
elif operator == "-":
    num1 - num2
    result = num1 - num2
# operator for *
elif operator == "*":
    num1 * num2
    result = num1 * num2
# operator for /
elif operator == "/":
    num1 / num2
    result = num1 / num2
print("----------") # for decoration
# print the result
print (round(result, 5)) # round    make the max lenght of the result lenght shorter
