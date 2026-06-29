'''---------- Employee Salary Statistics ----------

Find highest, lowest, average salary and
employees earning more than Rs.50000.

---------------------------------------------------'''

#--------------------------------------------------
#---------------- Coding --------------------------

n = int(input("Enter Number of Employees : "))

total = 0
highest = -1
lowest = 999999
count = 0

for i in range(n):

    salary = float(input("Enter Salary : "))

    total += salary

    if(salary > highest):
        highest = salary

    if(salary < lowest):
        lowest = salary

    if(salary > 50000):
        count += 1

average = total/n

print("Highest Salary :",highest)
print("Lowest Salary :",lowest)
print("Average Salary :",average)
print("Employees earning more than Rs.50000 :",count)

#--------------------------------------------------