# Tuple is a type of datastructures where you can store different values
# similar to list, except there are key differences

# ================================================================================
# ** Tuples are IMMUTABLE **
#    --> they CANNOT BE CHANGED or modified it once it has been created
#    --> syntax is also different
#           -- you define it with () instead of [] like you would do a list
# ================================================================================

coordinates = (4, 5)
# coordinates[1] = 10   this will not work in python
print(coordinates[0])
print(coordinates[1])

# can create a list of tuples
coordinates2 = [(4, 5), (5, 6), (80, 69)]
print(coordinates2)