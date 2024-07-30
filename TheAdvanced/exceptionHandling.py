
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("WHY'D YOU DIVIDE BY ZERO")
    print(err)
except TypeError:
    print("THAT'S NOT A NUMBER BRO")