
employee_file = open("employees.txt", "r")
# open("employees.txt", "w")     // write to the file
# open("employees.txt", "a")     // append to the end of the file
# open("employees.txt", "r+")    // read and write to a file

print(employee_file.readable())     # check if you can even read from the file
# print(employee_file.read())       # reads the entire file

# print(employee_file.readline())     # reads the first line
# print(employee_file.readline())     # reads the second line, etc.

# print(employee_file.readlines())       # puts everything in an array
# print(employee_file.readlines()[1])      # first element in the array

for employee in employee_file.readlines():
    print(employee)

employee_file.close()   # ALWAYS MAKE SURE TO CLOSE THE FILE YOU OPENED

