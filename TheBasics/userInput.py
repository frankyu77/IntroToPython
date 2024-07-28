
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Hello there " + user_name + "! You are " + user_age)

x = []
x.append(input("name an item you want to add: "))
print(x)
decision = input("Would you like to add another item? (Y/N) ")
while decision == "Y":
    x.append(input("enter another item you want to add"))
    print(x)
    decision = input("Would you still like to add another item? (Y/N)")
print(x)
print(user_name + " This is your final list. Thank you for participating")



