from math import *


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def power(a, b):
    return pow(a, b)


print("Welcome to Intermediate Calculator!")
num1 = int(input("Please enter in the first number: "))
operation = input("Please enter in the operator (+, -, *, /, ^): ")
num2 = int(input("Please enter in the second number: "))

if operation == "+":
    print(addition(num1, num2))
elif operation == "-":
    print(subtraction(num1, num2))
elif operation == "*":
    print(multiplication(num1, num2))
elif operation == "/":
    print(division(num1, num2))
elif operation == "^":
    print(power(num1, num2))
else:
    print("================================")
    print("Please enter a valid operator")

