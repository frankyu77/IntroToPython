
employee_file = open("employees.txt", "a")

employee_file.write("\nKelly - Customer Service")

employee_file.close()

# employee_file = open("employees.txt", "w")
#
# # this now OVERRIDES the  entire file and only puts this instead
# employee_file.write("\nKelly - Customer Service")
#
#
# employee_file.close()

# now creates new file because you made a new name
employee_file = open("employees1.txt", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

employee_file = open("index.html", "w")
employee_file.write("<p>THIS IS HTML</p>")
employee_file.close()