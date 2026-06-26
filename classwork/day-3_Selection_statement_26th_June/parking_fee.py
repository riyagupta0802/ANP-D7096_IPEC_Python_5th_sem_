'''---------- Parking Fee Waiver ------------------

A shopping mall waives the parking fee if a customer has
made purchases worth ₹2,000 or more. Otherwise, the customer
must pay a parking fee of ₹100.

Write a Python program to accept the purchase amount and
display whether the parking fee is waived or payable.

---------------------------------------------------------
Sample Input 1
Enter the purchase amount : 2500

Sample Output 1
Parking Fee Waived!
Parking Fee : ₹0

---------------------------------------------------------
Sample Input 2
Enter the purchase amount : 1500

Sample Output 2
Parking Fee Payable!
Parking Fee : ₹100

---------------------------------------------------------
Sample Test Cases

Test Case 1
Input : 2500
Output :
Parking Fee Waived!
Parking Fee : ₹0

Test Case 2
Input : 1500
Output :
Parking Fee Payable!
Parking Fee : ₹100

Test Case 3
Input : 2000
Output :
Parking Fee Waived!
Parking Fee : ₹0

Test Case 4
Input : -500
Output :
Purchase amount cannot be negative

---------------------------------------------------------'''
#--------------------------------------------------------------------
#--------- Coding ----------------------------------------------------

# input of purchase amount from the user
purchase_amount = float(input("Enter the purchase amount : "))

# validate the purchase amount
if(purchase_amount < 0):
    exit("Purchase amount cannot be negative")

#--------------------------------------------------------------
# checking whether parking fee is waived or not
if(purchase_amount >= 2000):
    print("Parking Fee Waived!")
    print("Parking Fee : ₹0")
else:
    print("Parking Fee Payable!")
    print("Parking Fee : ₹100")

#----------------------------------------------------

''' Output :
Enter the purchase amount : 2500
Parking Fee Waived!
Parking Fee : ₹0
'''