''' Electricity Bill Discount
-------------------------------------------------------
An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000
or more. Otherwise, no discount is applied.
---------------------------------------------------------



Sample Input 1
Enter the electricity bill amount: 6200
----------------------------------------------------------
Sample Output 1
Discount Applied!
----------------------------------------------------------
Sample Output 1
Final Bill Amount: ₹5580.0
----------------------------------------------------------
'''

#------- Coding ---------------

# input of electricity bill amount from the user
bill_amount = float(input("Enter the electricity bill amount : "))

# validate the bill amount
if(bill_amount < 0):
    exit("Bill amount cannot be negative")

#--------------------------------------------------------------
print("--------------------------------------------")

# check whether discount is applicable or not
if(bill_amount >= 5000):
    discount = bill_amount * 0.10
    final_amount = bill_amount - discount
    print("Discount Applied!")
    print("Final Bill Amount : ₹", final_amount)
else:
    print("No Discount Applied!")
    print("Final Bill Amount : ₹", bill_amount)

#----------------------------------------------------
'''Output :

Enter the electricity bill amount : 6200
--------------------------------------------
Discount Applied!
Final Bill Amount : ₹ 5580.0
--------------------------------------------

Enter the electricity bill amount : 4200
--------------------------------------------
No Discount Applied!
Final Bill Amount : ₹ 4200.0
--------------------------------------------
'''