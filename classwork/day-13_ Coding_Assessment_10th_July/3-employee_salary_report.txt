'''                        ---Employee Salary Report---

Create a Python program that stores employee details in a dictionary. 
Each employee should have: 
• Employee ID  
• Name  
• Salary  
Allow the user to enter details for 5 employees. 
After storing the data: 
1. Display all employee details.  
2. Find the employee having the highest salary.  
3. Display the average salary.  
---------------------------------
Sample Output 
Employee Details 
101 Rahul 45000 
102 Amit 52000 
103 Neha 48000 
104 Priya 60000 
105 Karan 55000 
 
Highest Salary 
Priya 60000 
 
Average Salary 
52000
'''

# Creating blank dict
employees = {}

# Input details of 5 employees
for i in range(5):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))

    employees[emp_id] = {"Name": name, "Salary": salary}

# Display employee details
print("Employee Details")
for emp_id in employees:
    print(emp_id, employees[emp_id]["Name"], employees[emp_id]["Salary"])

# Find employee with highest salary
highest_salary = 0
highest_name = ""

total_salary = 0

for emp_id in employees:
    salary = employees[emp_id]["Salary"]
    total_salary += salary

    if salary > highest_salary:
        highest_salary = salary
        highest_name = employees[emp_id]["Name"]

# Display highest salary
print("\nHighest Salary")
print(highest_name, highest_salary)

# Display average salary
average = total_salary / 5
print("\nAverage Salary")
print(average)

'''Output:
Sample Output 
Employee Details 
101 Rahul 45000 
102 Amit 52000 
103 Neha 48000 
104 Priya 60000 
105 Karan 55000 
 
Highest Salary 
Priya 60000 
 
Average Salary 
52000
'''