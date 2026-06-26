'''---------- Premium Membership Eligibility ------------------
A customer becomes Premium Member if:

• Total Purchases > ₹50000
• Orders Completed >= 20
• Customer Rating >= 4.5

Special Case:
• Purchases above ₹100000 automatically qualify.

--------------------------------------------------------------
Sample Input
Total Purchases : 120000
Orders Completed : 10
Customer Rating : 4.0
--------------------------------------------------------------
Sample Output
Premium Membership Status : Eligible
Reason : Purchase amount exceeded ₹100000.
--------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

purchase = float(input("Enter Total Purchases : "))
orders = int(input("Enter Orders Completed : "))
rating = float(input("Enter Customer Rating : "))

if(purchase < 0 or orders < 0 or rating < 0):
    exit("Invalid Input")

if(purchase > 100000):
    print("Premium Membership Status : Eligible")
    print("Reason : Purchase amount exceeded ₹100000.")
elif(purchase > 50000 and orders >= 20 and rating >= 4.5):
    print("Premium Membership Status : Eligible")
else:
    print("Premium Membership Status : Not Eligible")

#--------------------------------------------------------------

''' Output :
Enter Total Purchases : 120000
Enter Orders Completed : 10
Enter Customer Rating : 4.0

Premium Membership Status : Eligible
Reason : Purchase amount exceeded ₹100000.
'''