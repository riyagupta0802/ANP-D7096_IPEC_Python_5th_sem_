'''-------Employee Information System----------

Problem Statement:

Create a dictionary where: 
• Employee ID is the key.  
• Value is another dictionary containing:  
o Name  
o Department  
o Salary  

Perform the following operations: 
• Display all employee details.  
• Search for an employee using Employee ID.  
• Increase the salary of all employees by 10%.  
• Display employees belonging to a specific department entered by the user.'''


# initialize dictionary
employees = {}

# input details of 3 employees
for i in range(3):
    empid = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    employees[empid] = {"Name": name, "Department": department, "Salary": salary}
print("-------------------------------------------------")

# display all employee details
print("Employee Details:")
for empid in employees:
    print(empid, employees[empid])
print("-------------------------------------------------")

# search employee
empid = input("Enter Employee ID to Search: ")
if empid in employees:
    print(employees[empid])
else:
    print("Employee not found")
print("-------------------------------------------------")

# increase salary by 10%
for empid in employees:
    employees[empid]["Salary"] = employees[empid]["Salary"] + (employees[empid]["Salary"] * 10 / 100)

print("After 10% Salary Increase:")
for empid in employees:
    print(empid, employees[empid])
print("-------------------------------------------------")

# display employees of specific department
department = input("Enter Department to Search: ")
print("Employees in", department, "Department:")
for empid in employees:
    if employees[empid]["Department"] == department:
        print(empid, employees[empid])

'''Output:
Enter Employee ID: E101
Enter Employee Name: Rahul
Enter Department: HR
Enter Salary: 30000
Enter Employee ID: E102
Enter Employee Name: Priya
Enter Department: IT
Enter Salary: 45000
Enter Employee ID: E103
Enter Employee Name: Ankit
Enter Department: IT
Enter Salary: 40000
-------------------------------------------------
Employee Details:
E101 {'Name': 'Rahul', 'Department': 'HR', 'Salary': 30000.0}
E102 {'Name': 'Priya', 'Department': 'IT', 'Salary': 45000.0}
E103 {'Name': 'Ankit', 'Department': 'IT', 'Salary': 40000.0}
-------------------------------------------------
Enter Employee ID to Search: E102
{'Name': 'Priya', 'Department': 'IT', 'Salary': 45000.0}
-------------------------------------------------
After 10% Salary Increase:
E101 {'Name': 'Rahul', 'Department': 'HR', 'Salary': 33000.0}
E102 {'Name': 'Priya', 'Department': 'IT', 'Salary': 49500.0}
E103 {'Name': 'Ankit', 'Department': 'IT', 'Salary': 44000.0}
-------------------------------------------------
Enter Department to Search: IT
Employees in IT Department:
E102 {'Name': 'Priya', 'Department': 'IT', 'Salary': 49500.0}
E103 {'Name': 'Ankit', 'Department': 'IT', 'Salary': 44000.0}'''        