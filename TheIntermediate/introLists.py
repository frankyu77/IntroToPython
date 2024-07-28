
list = ["asdf", "asdf1", "asdf2", "water", "fire", "earth", "stone"]
list1 = ["asdf", 34, True, False]       # can store anything you want in the lsit

print(list)
print(list1)
print("3rd element of list1: " + str(list1[3]))

print(list1[-2])    # can use negative index to access elements from the back of the list
                    # first index starting from the back of the list is 1-based index
                    # first index starting from the front of the list is 0-based index
print(list[1:])     # all elements starting from index 1
print(list[1:3])    # all elements from index 1 to 3 (not inclusive of 3)

list[1] = "doodoo"
print(list)

