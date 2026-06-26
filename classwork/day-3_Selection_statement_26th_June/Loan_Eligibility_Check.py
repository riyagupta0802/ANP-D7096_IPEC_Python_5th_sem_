'''---------- Loan Eligibility Check ------------------

A bank considers an applicant eligible for a personal loan
only if their monthly salary is ₹30,000 or more.

Write a Python program to accept the applicant's monthly
salary and display whether they are eligible to apply
for the loan.

---------------------------------------------------------
Sample Input 1
Enter your monthly salary : 45000

Sample Output 1
Congratulations! You are eligible to apply for the loan.

---------------------------------------------------------
Sample Input 2
Enter your monthly salary : 22000

Sample Output 2
Sorry! You are not eligible to apply for the loan.

---------------------------------------------------------
Sample Test Cases

Test Case 1
Input : 45000
Output :
Congratulations! You are eligible to apply for the loan.

Test Case 2
Input : 22000
Output :
Sorry! You are not eligible to apply for the loan.

Test Case 3
Input : 30000
Output :
Congratulations! You are eligible to apply for the loan.

Test Case 4
Input : -5000
Output :
Salary cannot be negative

---------------------------------------------------------'''
#--------------------------------------------------------------------
#--------- Coding ----------------------------------------------------

# input of monthly salary from the user
salary = float(input("Enter your monthly salary : "))

# validate the salary
if(salary < 0):
    exit("Salary cannot be negative")

#--------------------------------------------------------------

# checking loan eligibility
if(salary >= 30000):
    print("Congratulations! You are eligible to apply for the loan.")
else:
    print("Sorry! You are not eligible to apply for the loan.")

#----------------------------------------------------

''' Output :
Enter your monthly salary : 45000
Congratulations! You are eligible to apply for the loan.
'''