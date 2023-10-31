

employee_file = open("Employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()  # you want to always close your files