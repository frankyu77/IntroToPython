from math import *


def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))


def addition(a, b):
    print("adding " + str(a) + " and " + str(b) + " = ")
    return a + b


def power(a, b):
    print("powering " + str(a) + " by " + str(b) + " = ")
    return pow(a, b)


say_hi("Mike", 35)
say_hi("Joe", 70)

print(addition(7, 8))
print(power(7, 8))

