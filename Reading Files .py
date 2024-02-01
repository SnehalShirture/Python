
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()




#print(employee_file.read())
#print(employee_file.readlines()[1])


#employee_file.close()