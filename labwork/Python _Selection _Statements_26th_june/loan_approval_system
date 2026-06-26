'''---------- Loan Approval System -------------------------
A bank evaluates loan applications using:

• Credit Score >= 750
• Annual Income >= ₹8,00,000
• Existing Loan <= ₹2,00,000

Conditions:
• All conditions satisfied -> Approved
• Only one condition fails -> Manual Review
• More than one condition fails -> Rejected

-----------------------------------------------------------
Sample Input
Enter Credit Score : 780
Enter Annual Income : 750000
Enter Existing Loan Amount : 100000
-----------------------------------------------------------
Sample Output
Loan Status : Manual Review
Reason : Income criteria not satisfied.
-----------------------------------------------------------'''
#----------------------------------------------------------
#---------------- Coding ----------------------------------

credit = int(input("Enter Credit Score : "))
income = float(input("Enter Annual Income : "))
loan = float(input("Enter Existing Loan Amount : "))

fail = 0

if(credit < 750):
    fail += 1

if(income < 800000):
    fail += 1

if(loan > 200000):
    fail += 1

if(fail == 0):
    print("Loan Status : Approved")
elif(fail == 1):
    print("Loan Status : Manual Review")

    if(credit < 750):
        print("Reason : Credit Score criteria not satisfied.")
    elif(income < 800000):
        print("Reason : Income criteria not satisfied.")
    else:
        print("Reason : Existing Loan criteria not satisfied.")
else:
    print("Loan Status : Rejected")

#----------------------------------------------------------

''' Output :
Enter Credit Score : 780
Enter Annual Income : 750000
Enter Existing Loan Amount : 100000

Loan Status : Manual Review
Reason : Income criteria not satisfied.
'''